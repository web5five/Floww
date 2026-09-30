# Run and contribute / 실행 및 작업 시작

Product code remains in four component repositories. The hub records release pins and evidence; cloning it alone does not start the application. 최상위 저장소는 코드 실행기가 아닌 통합·제출 진입점입니다.

## Obtain the code

```sh
git clone https://github.com/web5five/Floww.git
git clone https://github.com/web5five/Floww_Server.git
git clone https://github.com/web5five/Floww_Frontend_Client.git
git clone https://github.com/web5five/Floww_SmartContract.git
git clone https://github.com/web5five/Floww_Frontend_Admin.git
```

For a repeatable review, check out the full component SHAs in [release-manifest.json](../release-manifest.json). For active development, fetch the latest accepted main first and preserve existing work. Never mistake the evidence run's old runtime SHA for the latest component or deployment.

## Runtime and setup

| Component | Run instructions |
| --- | --- |
| Server | Java 21, PostgreSQL 16.4, Maven Wrapper and Flyway. Use the historical [container smoke runbook](https://github.com/web5five/Floww_Server/blob/153b5f3e78467f1dc5cbc8d58d9c86ee52aaf8c6/docs/CONTAINER_RUNTIME_KO_EN.md), placeholder `.env.example`, and `./mvnw -B verify` for build/tests. To start the API with a configured database/environment, run `./mvnw spring-boot:run`; health is `GET /actuator/health`. [TaskAccount configuration and API](https://github.com/web5five/Floww_Server/blob/153b5f3e78467f1dc5cbc8d58d9c86ee52aaf8c6/docs/TASKACCOUNT_E2E_KO_EN.md) governs the selected-purchase path. |
| Client | Node 24.19, pinned package lock: `npm ci`, configure `.env.local` from the example, then `npm run dev -- --port 3001`. Production: `npm run build` and `npm start -- --port 3001`. A configured backend and real owner session are required for business actions. |
| Admin | Node 24.19, pinned lock: `npm ci`, configure server-only `FLOWW_SERVER_URL`, then run the [Admin README](https://github.com/web5five/Floww_Frontend_Admin) commands. Requires an ADMIN login; do not promote a normal user as a shortcut. |
| Contract | Follow the pinned [Foundry build/test instructions](https://github.com/web5five/Floww_SmartContract/blob/d4e6a7d7b7635634b8a59f7c87bba91d3b311f9d/README.md). Tests do not require a fresh public deployment. Never rerun broadcast commands just to inspect an existing receipt. |

The server's historical fixture/API guides document older component checks. Use the [current frontend E2E handoff](https://github.com/web5five/Floww_Server/blob/153b5f3e78467f1dc5cbc8d58d9c86ee52aaf8c6/docs/FRONTEND_E2E_HANDOFF_KO_EN.md) together with the Client's [TaskAccount handoff](https://github.com/web5five/Floww_Frontend_Client/blob/5003d0a49d3a6c46c1055b178a722e9815f37ad7/docs/task-execution-handoff.md). The current TaskAccount mode uses its own account API sequence; legacy `confirmed:true` and `REVIEWED` do not grant spending authority.

## Environment boundaries

Keep Kiln, executor/reporter keys, session secrets and Preview access values server-only and outside Git. A Magic publishable key is the only intentionally public Magic configuration; do not put a secret key in `NEXT_PUBLIC_*`. Configure exact frontend origin and Sepolia chain IDs consistently. Missing settings must disable actions rather than synthesize results.

Redis, pgvector, Kafka, Eureka, Config Server, browser sandboxing and a separate Python service are not default runtime dependencies.

## Checks and handoff

- Client/Admin: pinned install, lint, typecheck, build and relevant browser/runtime tests. Fixtures test application behavior but do not prove a real provider or payment.
- Server: Java/PostgreSQL tests; inspect actual HTTP contracts and owner/role isolation. Read the evidence's recorded runtime identity before reproducing a live run.
- Contract: pinned Foundry tests and actual read-only chain evidence when needed.
- Hub: `python3 scripts/validate_manifest.py`. The structural check does not certify release readiness. `--complete` must fail while required live checks or final artifacts remain missing.

Record owned files and integration boundaries before parallel work. Use [CONTRIBUTING](../CONTRIBUTING.md), [worklog template](WORKLOG_TEMPLATE.md), and [release checklist](RELEASE_CHECKLIST.md). Keep final public evidence understandable without access to private Confluence. 최종 사용자 화면 검증·공개 증거·제출 파일은 모듈 테스트와 별도로 확인합니다.
