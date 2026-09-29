# Floww — Flow Wallet

Floww is a team project for bounded AI spending: the user confirms a mandate, the AI proposes actions, and deterministic checks enforce the permitted scope.

Floww는 사용자가 승인한 지출 범위 안에서 AI가 행동을 제안하고, 코드로 한도를 집행하는 팀 프로젝트입니다.

This is the integration and submission entry point. The currently runnable server slice validates a confirmed mandate, fetches a server-owned test quote, executes a bounded model/tool conversation, and persists owner-only evidence. The complete wallet-to-purchase experience is still being integrated.

현재 실행 가능한 서버는 확정된 구매 범위를 받아 테스트 견적과 모델의 도구 호출을 검증하고, 소유자별 실행 기록을 저장합니다. 지갑 승인부터 실제 구매까지 이어지는 전체 제품은 통합 중입니다.

## Run and inspect / 실행과 확인

1. Open [Start here](docs/START_HERE.md) and [server PR #3](https://github.com/web5five/Floww_Server/pull/3) for the implementation history. The component revisions below distinguish runnable server code from the frontend/admin/contract foundations.
2. Check [release-manifest.json](release-manifest.json) for the exact component revisions and their verification limits.
3. Use the [server setup and API contract](https://github.com/web5five/Floww_Server/blob/3f1fe3e228f2e6b151d56f2ac7d99efbae7704d2/docs/API_CONTRACT.md) with Java 21, Docker/PostgreSQL and Python 3 for test fixtures. No paid inference credential is needed for the local fixture path.
4. Follow the [technical walkthrough](https://github.com/web5five/Floww_Server/blob/3f1fe3e228f2e6b151d56f2ac7d99efbae7704d2/docs/TECHNICAL_DEMO.md). A real Kiln key is only required for explicitly labeled live-model validation.

설치 명령과 API 예제는 서버 문서를 기준으로 실행합니다. 테스트 판매자·테스트 모델·실제 Kiln·온체인 지급은 서로 다른 증거 단계이며, `REVIEWED`는 “사람이 검토할 견적 준비” 상태입니다.

## Repositories / 저장소

| Repository | Responsibility / 역할 | Current boundary / 현재 경계 |
| --- | --- | --- |
| [Server](https://github.com/web5five/Floww_Server) | Java AI/tools, quote validation, persisted events and evidence / AI·도구·견적·실행 기록 | Module verified; core auth, merchant and payment integration pending / 모듈 검증 완료·제품 통합 대기 |
| [Client](https://github.com/web5five/Floww_Frontend_Client) | Request, approval, progress, outcome / 요청·승인·진행·결과 화면 | Collaboration foundation; application not yet verified / 협업 기반만 확인 |
| [Admin](https://github.com/web5five/Floww_Frontend_Admin) | Operational UI if required / 필요한 경우 운영 화면 | Optional; no application scaffold assumed / 선택 구성 |
| [Contracts](https://github.com/web5five/Floww_SmartContract) | Wallet/chain boundary and verifiable receipts / 지갑·체인·영수증 | No deployed contract or settlement proof / 배포·지급 증거 없음 |

## Trust and evidence / 권한과 증거

The model may search offers, request a quote and propose a stored quote ID. It cannot supply a trusted price, recipient, signing authority or payment-success fact. Deterministic code checks scope and expiry; future wallet/core adapters must enforce authority again at settlement. The included merchant is a loopback test fixture and `TEST_USDC` is a test denomination. Local bearer tokens are development identities, not wallet approvals.

모델은 저장된 견적 ID를 제안하며, 가격·수신자·서명 권한·지급 성공을 임의로 확정할 수 없습니다. 현재 정책 검증을 최종 결제 집행이나 실제 사용자 승인으로 해석하면 안 됩니다.

See [observed module verification](docs/evidence/2026-09-29/README.md): 13 Java tests, 82 independent assertions, 7 Docker checks, and a real four-call Kiln conversation. These verify the server slice only.

Read the [release checklist](docs/RELEASE_CHECKLIST.md) and [integration issue](https://github.com/web5five/Floww/issues/3). Real chain evidence, the combined UI path, the final video and deck remain separate submission gates. A passing manifest check validates declarations, not a completed product.

## Collaboration and prior work / 협업과 선행 작업

Use [AGENTS.md](AGENTS.md), [CONTRIBUTING.md](CONTRIBUTING.md), the [worklog template](docs/WORKLOG_TEMPLATE.md), and [runtime readiness](docs/RUNTIME_READINESS.md). Public evidence must be readable without private Confluence access. Keep secrets and private team conversations outside Git.

Floww's server work extends the local F002/F004 implementation developed during this team's integration work. The product discussion drew on earlier PAIVERA planning; no PAIVERA implementation was copied into this server slice. Visible Orca GPT-6 Sol assisted implementation; the controller performed separate acceptance checks. Coding assistance is distinct from product inference, which uses event Kiln `qwen3-32b` for live runs. Authorized hackathon merges use controller review and required CI; domain decisions and product acceptance remain separately recorded.

이전 PAIVERA 기획에서 논의한 개념과 Floww의 실제 코드를 구분합니다. AI 코딩 지원·독립 검증·실제 제품 추론·팀원 승인은 각각 별도로 기록합니다.
