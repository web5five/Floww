# Working together / 협업 절차

Use a GitHub issue for actionable work, a component PR for code, and Confluence for bilingual decisions and handoffs. Telegram is for short coordination; do not make chat the only copy of an interface or decision.

GitHub 이슈에 실행할 작업, 컴포넌트 PR에 코드, Confluence에 한영 결정·인계를 기록합니다. 텔레그램에서 결정한 계약도 문서와 연결합니다.

1. Search for an existing issue. Name the outcome, owner, owned files, dependencies and observable acceptance. Cross-repository work has a hub issue linked from component issues.
2. Read `AGENTS.md`, current source versions and Git status. Use feature/, fix/, docs/ or chore/ branches. Preserve teammate edits and remote history.
3. Confirm shared contracts before dependent code: identifiers, units, status/error codes, authentication, idempotency, migration and payment authority.
4. Implement one bounded slice. Run the exact repository build/test and a meaningful runtime path. Record failures as failures.
5. Open a Draft PR with evidence. `Closes #N` closes only work this PR fully satisfies; reference the integration issue without closing it early.
6. Record controller/agent review and seek relevant domain-owner feedback for shared auth/schema/payment/signing changes. During the hackathon, teammate approval is recommended but is not a mandatory merge gate. Never present controller/AI review as human approval.
7. After review and actual required CI pass, merge within the task's authorization. After conflict resolution, inspect the combined behavior/contracts and rerun affected checks against the resulting head. Validate combined component SHAs, update `release-manifest.json`, then close the integration issue only when its full acceptance criteria pass.
8. Write a concise bilingual Confluence worklog with issue/PR links, changed paths, tests, limits and next owner. Read latest page before writing, preserve unrelated edits and read back the stored version. If MCP fails, keep `PENDING_SYNC`; do not claim publication.

작업 이슈 → 계약 확인 → 구현 → 실제 검증 → Draft PR → 독립 리뷰 → 허용된 병합 → 통합 SHA 확인 → 한영 기록 순서입니다. CI 성공·팀원 승인·실제 온체인 증거를 서로 대신하지 않습니다.

해커톤 기간에는 컨트롤러/에이전트 리뷰와 필수 CI를 통과하면 권한 범위 안에서 팀원 승인 대기 없이 병합합니다. 사람이 승인했다고 기록하지 않으며, 충돌 해결 후에는 결과 코드의 의미와 관련 검사를 다시 확인합니다. 제품의 승인·지급 권한은 그대로 유지합니다.

## Ownership / 담당 경계

- Client: request, mandate approval, progress, outcome and recovery UX.
- Server core: auth, state, reservations, idempotency, durable recovery and migrations.
- Server AI/evidence: Kiln/tool integration, validated events, history/export, evaluations and technical demo.
- Wallet/chain: custody, trusted mandate, signing, broadcasting, gas and reconciliation.
- Product: scenario, decision resolution, deck and rehearsal.

No contribution percentages. Do not assign unverified GitHub usernames. Add CODEOWNERS only after verifying real handles and repository access.

## Bootstrap and repository controls / 초기 구성과 저장소 설정

An empty repository may receive a small foundation commit to establish `main`; substantive implementation is reviewed in a PR. Required CI contexts must exist and pass before adding a rule referencing them. The hackathon policy uses zero required teammate approvals, resolved conversations, real required status checks, no force pushes and no default-branch deletion. Keep administrators subject to these rules. Hub requires `manifest`; server requires `verify`; the foundation-only components must add real application CI when code is introduced. Do not claim human approval or bypass failed checks. Read back GitHub settings before claiming a rule is configured.

Public issues, PRs and evidence exclude private team conversations, credentials, raw environment values and personal data. Engineering docs clearly distinguish fixture tests, live model calls, testnet settlement and user acceptance.

## Baseline / 기본 구성

One modular Java server and PostgreSQL are the working recommendation. Redis, pgvector, Kafka, Eureka and Config Server are deferred. Browser sandbox and a separate Python inference service are not required baseline services. Frontend/admin/contract repositories should not receive unnecessary frameworks just because they exist.

Every component owns its dependency lock or build wrapper, pinned runtime, env example, migrations where applicable, health check and real CI. This hub does not install every component automatically.
