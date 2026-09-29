# Architecture demonstration handoff / 핵심 아키텍처 데모 인계

This is an integration recommendation, not proof of a completed Floww purchase or unanimous team acceptance. Keep broader consumer services and fiat infrastructure in the long-term product vision while proving one bounded journey.

통합 추천안이며 전체 구매 완료나 팀 전체 합의를 뜻하지 않습니다. 하나의 제한된 여정을 실제로 연결하는 데 집중하고, 다양한 소비자 서비스와 법정화폐 인프라는 장기 비전으로 설명합니다.

## One journey / 하나의 여정

1. **Identity and wallet:** Magic email/embedded-wallet onboarding is the proposed mainstream path. Validate the actual authenticated user and associated wallet server-side. Login and wallet creation do not authorize AI spending. / 이메일 인증·지갑 매핑을 서버에서 확인하며 로그인 자체를 지출 승인으로 처리하지 않습니다.
2. **Funding:** select one testnet, one test asset and a gas source together. Wallet-to-wallet test funding is the recommended demonstration path; fiat/card onboarding can follow later. Confirm actual balances through the selected network. / 테스트넷·테스트 자산·가스 공급을 함께 정하고 실제 잔액을 조회합니다. 테스트 자산을 실제 달러 잔액으로 표현하지 않습니다.
3. **Draft:** F008 returns missing-condition questions or a structurally complete proposal. The user sees purpose, scope, provider eligibility, full cost, deadline and expected result. / 누락 조건을 질문하고 완성된 초안을 사용자에게 제시합니다.
4. **Exact confirmation:** F009 prepares the immutable review and binds a trusted confirmation receipt to the same owner, task, revision and digest. Changing any reviewed term requires a new review/confirmation. / 사용자가 확인한 초안과 현재 버전이 일치해야 하며 변경 후 이전 확인을 재사용하지 않습니다.
5. **Execution mandate:** core backend and wallet owners translate confirmed terms into enforceable chain/asset/recipient/amount/expiry restrictions and establish real authorization. Neither F008 readiness nor F009 binding is that authority. / 최종 실행 권한은 별도 인증·지갑 경계에서 만들고 집행합니다.
6. **Kiln and controls:** actual qwen3-32b proposes a stored authoritative quote ID. The deterministic executor and final signer enforce current authorization, cost, recipient, expiry, cancellation and idempotency. / 모델이 견적 ID를 제안하고 실행 경계에서 권한을 재검사합니다.
7. **Result:** record actual transaction/receipt and observable fulfillment against the same task/execution lineage. A submitted or paid order is not automatically fulfilled. / 거래와 수령 결과를 같은 실행 계보에 연결하고 주문 접수·지급·수령을 구분합니다.

## Integration checklist / 연동 점검

| Boundary / 경계 | Proposed consumer / 연결 담당 제안 | Required evidence / 확인할 것 |
| --- | --- | --- |
| Conversation → review | Frontend + AI / 프런트·AI | Missing conditions asked; exact current summary shown / 누락 질문과 현재 요약 |
| Review → confirmation | Core auth/backend + frontend / 인증·백엔드·프런트 | Authenticated owner; current task/revision; protected stored receipt / 실제 인증·현재 버전·보호된 확인 기록 |
| Confirmation → mandate | Core backend + wallet / 백엔드·지갑 | Enforceable recipients/assets/fees/expiry; cancellation and budget reservation / 실행 가능한 제한·취소·예산 예약 |
| Model → action | AI + core backend / AI·백엔드 | Actual tool call/usage; trusted merchant quote; bounded retries / 실제 도구·사용량·신뢰 견적 |
| Action → settlement | Wallet + core backend / 지갑·백엔드 | Final atomic checks; chain receipt; unknown-outcome reconciliation / 최종 검사·영수증·불명 거래 조회 |
| Settlement → result | Backend + frontend / 백엔드·프런트 | Verified fulfillment; simple result/recovery UI / 수령 검증·결과·복구 화면 |

These are coordination boundaries, not newly assigned teammate tasks. / 연결 경계이며 새 업무 배정이나 담당자 수락을 뜻하지 않습니다.

## Demonstration evidence / 시연 증거

- One successful bounded journey with actual inference, real authorization, testnet receipt and result. / 정상 여정 한 건.
- One incomplete or changed mandate blocked before execution; one action exceeding the approved scope blocked at the real execution boundary. / 불완전·변경 위임 차단과 승인 범위 밖 실행 차단.
- Keep component unit tests, local fixtures, live provider evidence, testnet settlement and user acceptance distinct. Do not close the integration issue for component-only checks. / 모듈 검사와 전체 실행 증거를 구분합니다.

Before connecting payment, agree the concrete service, eligible provider mapping, exact completion criterion, selected chain/token, fee/gas coverage and the final authorization mechanism. F009 avoids deciding those on other owners' behalf.

지급 연결 전에는 실제 서비스·제공자 매핑·완료 기준·체인/토큰·수수료/가스 범위·최종 권한 방식을 맞춥니다. F009가 이 결정을 대신하지 않습니다.

## Implemented component handoff / 구현된 컴포넌트 연결

Server source: `d5ecca8817157af3f19c62829a0745f12e22490e` ([F010 PR #10](https://github.com/web5five/Floww_Server/pull/10)). The component pin is not a release acceptance claim.

- [F008 AI draft contract](https://github.com/web5five/Floww_Server/blob/014c97f7f8f9111648aa26ff06aa3491cf377876/docs/AI_DRAFT_CONTRACT.md): missing-condition questions and structurally complete proposals. Prior [F008 evidence](https://github.com/web5five/Floww_Server/blob/0866189cd801cc2d4b381204bf31cd4ae5efed60/docs/evidence/f008/README.md) includes one live Kiln draft call at its recorded source.
- [F009 confirmation binding contract](https://github.com/web5five/Floww_Server/blob/014c97f7f8f9111648aa26ff06aa3491cf377876/docs/REVIEW_CONFIRMATION_BINDING.md): exact review snapshot, trusted current receipt and current server state comparison. [F009 evidence](https://github.com/web5five/Floww_Server/blob/014c97f7f8f9111648aa26ff06aa3491cf377876/docs/evidence/f009/README.md) records 55 passing Java/PostgreSQL tests, including 13 binding tests; no live wallet/approval/payment run.

F010 now exposes F008 through authenticated development transport `POST /api/ai/drafts`; F009 remains a Java confirmation-binding component. The current bearer identity is a local test principal. Core backend and frontend owners still integrate real Magic authentication and durable confirmation. The digest is an opaque server-produced review reference, not a signature or client-side spending credential.

F010으로 F008 초안을 개발용 HTTP 경로에서 호출할 수 있습니다. F009는 Java 확인 검사이며 실제 Magic 인증·확인 기록 저장은 담당자가 연결해야 합니다. 개발 토큰과 검토 다이제스트는 실제 사용자 지갑 또는 지출 권한을 증명하지 않습니다.

Keep [the end-to-end integration issue](https://github.com/web5five/Floww/issues/3) open until the combined revisions demonstrate actual authorization, model/tool usage, policy blocks, chain receipt and fulfillment/result.


## Callable draft API / 호출 가능한 초안 API

- [F010 bilingual HTTP contract](https://github.com/web5five/Floww_Server/blob/d5ecca8817157af3f19c62829a0745f12e22490e/docs/AI_DRAFT_HTTP.md): exact request/envelope, curl, status/error codes, conversation and byte limits. / 요청·응답·오류·예제.
- [F010 verification](https://github.com/web5five/Floww_Server/blob/d5ecca8817157af3f19c62829a0745f12e22490e/docs/evidence/f010/README.md): 60 passing Java/PostgreSQL tests, 15 independent packaged HTTP checks, and one actual Kiln HTTP call with 1,170 reported tokens. No real-user approval or payment proof. / 모듈·실제 모델 호출 증거이며 지갑·지급 증거는 아닙니다.

Send a user conversation through trusted server-side integration. Show clarification questions, append the user's answer, then show the returned objective, item scope, provider criteria, total cost with fees, absolute deadline and fulfillment criterion. Put model evidence under details. Keep development bearer and Kiln secrets out of browser source. Do not convert READY_FOR_REVIEW to legacy confirmed=true.

신뢰할 수 있는 서버 측 연결로 대화를 보내고, 누락 조건에 답한 뒤 여섯 가지 초안 조건을 보여줍니다. 모델 증거는 상세 보기로 두고, 개발용 Bearer·Kiln 키를 브라우저에 넣지 않습니다. 검토 가능한 초안을 자동 승인으로 처리하지 않습니다.

Next: replace test identity with verified Magic identity; persist the current owner/task/revision and authentic confirmation for F009; connect enforceable wallet authorization and settlement. These remain coordination boundaries, not automatically assigned or accepted tasks. / 다음은 실제 인증·확인 저장·지갑 권한·지급 연결이며 담당자 협의가 필요합니다.
