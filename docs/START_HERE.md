# Start here / 아침 작업 시작 안내

Use the hub for shared contracts, evidence and handoff. Code remains in the four component repositories. The parent workspace is not a Git repository.

최상위 Floww는 통합·제출 진입점이며 제품 코드는 각 저장소에서 작업합니다. 로컬 상위 작업 폴더 전체를 커밋하지 않습니다.

## First ten minutes / 첫 10분

1. Read your repository's `AGENTS.md`, current issue and the linked PR ([server #3](https://github.com/web5five/Floww_Server/pull/3), [hub #2](https://github.com/web5five/Floww/pull/2)). Fetch before editing, inspect the diff and declare owned files.
2. Read the current [system architecture](https://w3ph4ai.atlassian.net/wiki/spaces/GH/pages/11927569) and [engineering workflow](https://w3ph4ai.atlassian.net/wiki/spaces/GH/pages/12517414). Record the versions you used. Published recommendations still need the relevant owners' review.
3. Agree the shared API/state/event boundary before parallel implementation. The Java AI/evidence slice is a starting point for integration, not a replacement for production auth or payment state.
4. Use a focused branch, run the real check commands and open a PR with evidence. One independent teammate approval is required on protected default branches. Never force-push or silently bypass review.
5. Record a concise Korean/English handoff under the engineering workflow using Atlassian MCP, linking the real issue, PR, commit and checks. If unavailable, keep a local `PENDING_SYNC` record.

각 담당자는 착수 전에 원격 변경·작업 범위·문서 버전을 확인하고 공유 계약을 맞춥니다. 검증 결과는 실제 실행 여부까지 구분하여 이슈·PR·한영 작업 기록에 연결합니다.

## Component boundaries / 구성요소 경계

| Repository | Work to start / 착수할 일 | Existing foundation / 준비된 기반 |
| --- | --- | --- |
| [Server](https://github.com/web5five/Floww_Server) | Integrate AI/evidence with production auth, migration, durable execution and wallet path / 인증·마이그레이션·지속 실행·지갑 연결 | Java 21 implementation under review; use the PR README for exact commands / 구현 PR의 실행 문서 확인 |
| [Client](https://github.com/web5five/Floww_Frontend_Client) | Review Next.js choice and consume agreed progress/result contracts / Next.js 선택 검토·상태 계약 연결 | Collaboration instructions/templates; application and lockfile not yet implemented / 협업 기반만 준비 |
| [Admin](https://github.com/web5five/Floww_Frontend_Admin) | Start only if selected scenario needs it / 시나리오에 필요할 때 착수 | Optional, no application or dependency installation / 선택 구성 |
| [Contracts](https://github.com/web5five/Floww_SmartContract) | Decide task wallet versus custom contract, chain/asset/funding and receipt contract / 지갑·체인·자금·영수증 계약 | Collaboration instructions/templates; no deployed contract implied / 배포 완료 아님 |

Redis, pgvector, Kafka, Eureka, Config Server, browser sandboxing and a separate Python service remain outside the default runtime. Add any only after a documented need and owner review.

## Credentials and local environment / 계정·로컬 환경

- Use team9 only. Keep Kiln credentials in the server environment or approved secret store; never in browser code, Git, issues, Confluence or screenshots.
- Local development bearer tokens are test principals. They do not establish wallet ownership or production login.
- The Java module uses PostgreSQL and Maven Wrapper. Check its current README before running; do not install frontend/admin dependencies until those applications exist.
- A health response only proves the process is up. Missing merchant/payment integrations remain unavailable.
- Stop the specific processes you start; do not stop unrelated team or personal services. Do not delete shared databases during cleanup.

## Review and submit / 리뷰·제출

Use [CONTRIBUTING](../CONTRIBUTING.md), [worklog template](WORKLOG_TEMPLATE.md), and [release checklist](RELEASE_CHECKLIST.md). A protected branch and passing structural manifest check do not prove a working purchase. Only mark a release verified after checking the combined revisions, real inference, payment evidence, UI path and required submission artifacts.

리뷰 가능한 구현과 심사 제출 완료를 구분합니다. 최종 공개 README와 실행 증거는 팀 전용 Confluence 접근 없이도 확인할 수 있어야 합니다.
