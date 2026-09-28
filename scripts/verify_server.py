"""Controller acceptance against packaged Java, real Postgres and independent HTTP fixtures."""
from pathlib import Path
import concurrent.futures
import datetime as dt
import http.server
import hashlib
import json
import os
import secrets
import subprocess
import threading
import time
import urllib.error
import urllib.request
import uuid

SERVER = Path(os.environ['FLOWW_SERVER_PATH']).resolve()
OUT = Path(__file__).resolve().parents[1]/'.local/controller-verification'
OUT.mkdir(parents=True, exist_ok=True)
JDK = Path(os.environ['JAVA_HOME'])
BASE = 'http://127.0.0.1:18085'
state = {'case':'normal', 'calls':[], 'quoteExpiry':None, 'quoteId':'quote_controller'}

def iso(seconds=3600):
    return (dt.datetime.now(dt.timezone.utc)+dt.timedelta(seconds=seconds)).isoformat()

class Fixtures(http.server.BaseHTTPRequestHandler):
    def log_message(self,*args): pass
    def reply(self,data,code=200):
        data=json.dumps(data).encode();self.send_response(code)
        self.send_header('Content-Type','application/json')
        self.send_header('Content-Length',str(len(data)))
        self.send_header('X-Neocloud-Generation-Id','controller-fixture-only')
        self.end_headers();self.wfile.write(data)
    def do_GET(self):
        if self.path.startswith('/offers?'):
            return self.reply({'offers':[{'offerId':'offer_controller','itemId':'item_controller'}]})
        if self.path.startswith('/quotes?'):
            q={'quoteId':state['quoteId'],'offerId':'offer_controller','itemId':'item_controller',
               'totalCost':'9.50','currency':'TEST_USDC','recipient':'merchant_good',
               'expiresAt':state['quoteExpiry'] or iso()}
            if state['case']=='budget':q['totalCost']='10.01'
            if state['case']=='recipient':q['recipient']='merchant_wrong'
            if state['case']=='item':q['itemId']='item_wrong'
            if state['case']=='stale':q['expiresAt']=iso(-30)
            return self.reply(q)
        self.reply({'error':'not found'},404)
    def do_POST(self):
        data=json.loads(self.rfile.read(int(self.headers['Content-Length'])))
        state['calls'].append(data)
        n=sum(m['role']=='tool' for m in data['messages'])
        names=['search_offers','get_quote','propose_purchase']
        args=[{'itemId':'item_controller'},{'offerId':'offer_controller'},{'quoteId':state['quoteId']}]
        case=state['case'];final=n==3
        if case in ('slow_final','slow_mandate') and final:time.sleep(4)
        if case=='retry_once' and len(state['calls'])==1:return self.reply({'error':'busy'},503)
        if case=='auth_error':return self.reply({'error':'denied'},401)
        msg={'role':'assistant','content':'Reviewed locally; payment unavailable.' if final else None}
        if not final:
            arg=args[n].copy();name=names[n];cid='call_'+str(n)
            if case=='duplicate_id' and n==1:cid='call_0'
            if case=='unknown_tool' and n==0:name='send_payment'
            if case=='fabricated_quote' and n==2:arg={'quoteId':'made_up_quote'}
            if case=='override_price' and n==2:arg['totalCost']='0.01';arg['recipient']='merchant_wrong'
            msg['tool_calls']=[{'id':cid,'type':'function','function':{'name':name,'arguments':json.dumps(arg)}}]
        response={'model':'qwen3-32b','choices':[{'index':0,'finish_reason':'stop' if final else 'tool_calls','message':msg}],
                  'usage':{'prompt_tokens':100,'completion_tokens':20,'total_tokens':120}}
        if case=='truncated':response['choices'][0]['finish_reason']='length'
        if case=='missing_usage':response.pop('usage')
        self.reply(response)

def req(method,path,token=None,body=None,key=None):
    headers={'Content-Type':'application/json'}
    if token:headers['Authorization']='Bearer '+token
    if key:headers['Idempotency-Key']=key
    r=urllib.request.Request(BASE+path,method=method,headers=headers,data=None if body is None else json.dumps(body).encode())
    try:
        with urllib.request.urlopen(r,timeout=130) as v:return v.status,json.load(v)
    except urllib.error.HTTPError as e:
        return e.code,json.loads(e.read())

def main():
    env=os.environ.copy()
    for line in (SERVER/'.env').read_text().splitlines():
        if line and not line.startswith('#') and '=' in line:
            k,v=line.split('=',1);env[k]=v
    database='floww_tools_audit_'+uuid.uuid4().hex[:10]
    subprocess.run(['docker','exec','floww_server-db-1','createdb','-U','floww',database],check=True)
    env.update(FLOWW_PORT='18085',FLOWW_DB_URL='jdbc:postgresql://127.0.0.1:55433/'+database,
               KILN_BASE_URL='http://127.0.0.1:18999/v1',KILN_API_KEY='local-controller-fixture',
               FLOWW_TEST_MERCHANT_BASE_URL='http://127.0.0.1:18998',
               FLOWW_DEV_TOKEN_ALICE=secrets.token_hex(24),FLOWW_DEV_TOKEN_BOB=secrets.token_hex(24))
    alice,bob=env['FLOWW_DEV_TOKEN_ALICE'],env['FLOWW_DEV_TOKEN_BOB']
    servers=[http.server.ThreadingHTTPServer(('127.0.0.1',p),Fixtures) for p in (18998,18999)]
    for s in servers:threading.Thread(target=s.serve_forever,daemon=True).start()
    log=(OUT/'F004-controller-app.log').open('a');process=None
    report={'mode':'controller_http_fixtures_actual_postgresql','database':database,'checks':[],'runs':[],
            'jarSha256':hashlib.sha256((SERVER/'target/floww-server-0.1.0.jar').read_bytes()).hexdigest()}
    def check(label,condition):
        report['checks'].append({'name':label,'passed':bool(condition)})
        print(('PASS ' if condition else 'FAIL ')+label,flush=True)
        if not condition:raise AssertionError(label)
    def start():
        nonlocal process
        process=subprocess.Popen([str(JDK/'bin/java'),'-Xmx192m','-jar',str(SERVER/'target/floww-server-0.1.0.jar')],env=env,stdout=log,stderr=subprocess.STDOUT)
        for _ in range(150):
            if process.poll() is not None:raise RuntimeError('Application exited')
            try:
                if req('GET','/actuator/health')[0]==200:return
            except OSError:pass
            time.sleep(.2)
        raise RuntimeError('Application not healthy')
    def stop():
        nonlocal process
        if process and process.poll() is None:
            process.terminate()
            try:process.wait(timeout=10)
            except subprocess.TimeoutExpired:process.kill();process.wait()
        process=None
    def mandate(expiry=None):
        return {'confirmed':True,'mandate':{'goal':'Obtain the authorized test item','itemId':'item_controller',
                'maxTotal':'10.00','currency':'TEST_USDC','recipient':'merchant_good','expiresAt':expiry or iso()}}
    def events(data):return data['events']['events']
    def create(body,key=None):
        code,data=req('POST','/api/executions',alice,body,key or str(uuid.uuid4()))
        check('confirmed mandate creation',code==200);return data['id']
    def run(case,expected='REJECTED',expiry=None):
        state.update(case=case,calls=[],quoteExpiry=expiry,quoteId='quote_'+uuid.uuid4().hex[:10])
        eid=create(mandate(iso(2) if case=='slow_mandate' else None));code,data=req('POST','/api/executions/'+eid+'/run',alice)
        check(case+' status '+expected,code==200 and data.get('status')==expected)
        ev=req('GET','/api/executions/'+eid+'/evidence.json',alice)[1]
        report['runs'].append({'case':case,'evidence':ev})
        check(case+' never claims payment',str(ev.get('paymentStatus','')).startswith('NOT_AVAILABLE'))
        return eid,ev
    try:
        start();check('anonymous denied',req('GET','/api/executions')[0]==401)
        eid,normal=run('normal','REVIEWED')
        check('four calls bounded',len(state['calls'])==4)
        for n,request in enumerate(state['calls']):
            tools=[m for m in request['messages'] if m['role']=='tool']
            calls=[c['id'] for m in request['messages'] if m['role']=='assistant' for c in m.get('tool_calls',[])]
            check('tool results bound to original IDs turn '+str(n),len(tools)==n and [m['tool_call_id'] for m in tools]==calls)
        check('server-owned price recorded',any(e['kind']=='QUOTE_STORED' and e['payload'].get('totalCost')=='9.50' for e in events(normal)))
        check('complete terminal export declared',normal.get('complete') is True and normal.get('evidenceMode')=='local_test_merchant')
        check('local model never mislabeled Kiln',normal.get('modelEvidenceMode')=='local_model_fixture' and all(e.get('modelEvidenceMode')=='local_model_fixture' and e.get('source')=='local_model_fixture' for e in events(normal) if e['kind']=='MODEL_RESPONSE'))
        partial=req('GET','/api/executions/'+eid+'/evidence.json?limit=2',alice)[1]
        check('partial evidence never declared complete',partial.get('complete') is False and partial['events']['hasMore'])
        check('event correlation/version/source',all(e.get('schemaVersion') and str(e.get('correlationId'))==eid and e.get('source') for e in events(normal)))
        for path in ['', '/events','/evidence.json']:
            check('cross-owner denied '+path,req('GET','/api/executions/'+eid+path,bob)[0]==404)
        for case,code in [('budget','BUDGET_EXCEEDED'),('recipient','RECIPIENT_NOT_ALLOWED'),('item','ITEM_NOT_ALLOWED'),('stale','QUOTE_STALE'),('fabricated_quote','UNKNOWN_QUOTE_ID'),('override_price','INVALID_TOOL_ARGUMENTS'),('duplicate_id','DUPLICATE_TOOL_CALL_ID'),('unknown_tool','TOOL_NOT_ALLOWED')]:
            _,ev=run(case)
            check(case+' rejection persisted',events(ev)[-1]['payload'].get('code')==code)
        _,truncated=run('truncated','FAILED')
        tm=[x for x in events(truncated) if x['kind']=='MODEL_RESPONSE']
        check('truncated response retains reported usage',len(tm)==1 and tm[0]['payload']['usage'].get('total_tokens')==120)
        _,retried=run('retry_once','REVIEWED')
        rm=[x for x in events(retried) if x['kind']=='MODEL_RESPONSE']
        check('retried attempt usage marked unknown',len(rm)==5 and rm[0]['payload']['usageStatus']=='unknown')
        check('retry aggregate does not claim complete usage',retried.get('modelUsage',{}).get('status')=='incomplete')
        run('auth_error','FAILED')
        check('provider authentication never retried',len(state['calls'])==1)
        _,unknown=run('missing_usage','REVIEWED')
        models=[x for x in events(unknown) if x['kind']=='MODEL_RESPONSE']
        check('unknown usage not fabricated',len(models)==4 and all(m['payload']['usageStatus']=='unknown' and not m['payload']['usage'] for m in models))
        run('slow_final','REJECTED',iso(2))
        run('slow_mandate','REJECTED')
        body=mandate();key=str(uuid.uuid4());item=create(body,key)
        check('created execution export not terminal',req('GET','/api/executions/'+item+'/evidence.json',alice)[1].get('complete') is False)
        check('idempotency same execution',req('POST','/api/executions',alice,body,key)[1].get('id')==item)
        changed=json.loads(json.dumps(body));changed['mandate']['itemId']='different'
        check('idempotency protects item scope',req('POST','/api/executions',alice,changed,key)[0]==409)
        state.update(case='normal',calls=[],quoteExpiry=None)
        with concurrent.futures.ThreadPoolExecutor(2) as pool:
            results=list(pool.map(lambda _:req('POST','/api/executions/'+item+'/run',alice),range(2)))
        check('concurrent run only executes once',sorted(r[0] for r in results)==[200,409] and len(state['calls'])==4)
        page=req('GET','/api/executions/'+eid+'/events?limit=2',alice)[1];combined=page['events'][:]
        while page['hasMore']:
            page=req('GET','/api/executions/'+eid+'/events?limit=2&after='+str(page['nextCursor']),alice)[1]
            combined+=page['events']
        check('all event pages complete and unique',combined==events(normal) and len({e['seq'] for e in combined})==len(combined))
        hp=req('GET','/api/executions/history?limit=3',alice)[1];history=hp['executions'][:]
        while hp['hasMore']:
            hp=req('GET','/api/executions/history?limit=3&before='+hp['nextCursor'],alice)[1]
            history+=hp['executions']
        expected=req('GET','/api/executions?limit=100',alice)[1]
        check('history cursor covers all owned executions once',[x['id'] for x in history]==[x['id'] for x in expected] and len({x['id'] for x in history})==len(history))
        check('foreign history anchor hidden',req('GET','/api/executions/history?before='+eid,bob)[0]==404)
        stop();start();after=req('GET','/api/executions/'+eid+'/evidence.json',alice)[1]
        check('restart preserves evidence',after==normal)
        check('credentials not exported',all(t not in json.dumps(report) for t in [alice,bob,env['KILN_API_KEY']]))
        report['passed']=True
    except Exception as e:
        report.update(passed=False,errorType=type(e).__name__,error=str(e));raise
    finally:
        stop()
        for s in servers:s.shutdown();s.server_close()
        log.close();(OUT/'F004-controller.json').write_text(json.dumps(report,indent=2)+'\n')

if __name__=='__main__':main()
