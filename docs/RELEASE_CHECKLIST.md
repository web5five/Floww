# Release checklist / 제출 점검

This is a checklist, not a claim that any unchecked item is complete.

- [ ] One-sentence capability declaration matches the running implementation.
- [ ] Final runtime inference uses Kiln `qwen3-32b`; coding assistants are distinguished.
- [ ] Actual tool calls, usage, provider generation IDs and failures are recorded without credentials.
- [ ] At least one verifiable on-chain transaction; identify chain, asset and real transaction hash. For devnet, provide reproduction scripts/logs/reviewable code.
- [ ] If Challenge B is selected: two different out-of-scope attempts are blocked and logged at the execution boundary.
- [ ] If Challenge A is selected: two changed budget/deadline runs including refusal.
- [ ] Fresh-clone run instructions and all required component SHAs are verified together.
- [ ] Wallet, merchant, core-state and UI owners have reviewed their integration boundaries.
- [ ] Demo of actual operation is at most 3 minutes; deck PDF at most 10 pages.
- [ ] Prior work and AI assistance are disclosed; no copied private conversations or credentials.
- [ ] Final form, links, Git history and submission confirmation are preserved by the submission owner before the deadline.

현재 확인한 행사 마감은 2026-09-30 12:00 KST이며 최종 제출 폼과 공지는 제출 담당자가 다시 확인합니다. 이 저장소 생성은 제출 행위가 아닙니다.

The recorded deadline is 2026-09-30 12:00 KST. The submission owner must recheck the final form and announcements. Creating this repository is not a contest submission.

## Release manifest

`python3 scripts/validate_manifest.py` checks structure and declared evidence paths without pretending unfinished components are ready. `python3 scripts/validate_manifest.py --complete` is the stricter release gate: required revisions and every evidence category must be present, and `releaseStatus` must be `verified`. A manifest never replaces review of the referenced evidence.

Use immutable 40-character component commit SHAs, not moving branches. SHA availability and runtime behavior must be independently checked before changing a component's status to `verified`.

## Recording and judge-access readiness

This local checklist separates recorded facts from work the submission/deployment owners still need to finish. It does not authorize a cloud setting change, load test or final submission.

| Status | Check |
| --- | --- |
| Verified source selection | The user shared an [eight-slide Google Slides source](https://docs.google.com/presentation/d/1GFQ5FflJ9HU2TjGv9FYD5zU2wfm_Hsfc/edit). Viewer permissions, final content and exported PDF have not been checked here. |
| Pending recording | Record an actual operation in at most 3 minutes, with the correct hosted-versus-F031 evidence labels; inspect the exported video and keep personal emails, OTPs, credentials, private keys and protection-bypass URLs/tokens out of frames and narration. Do not fabricate missing payment or C results. |
| Pending stable link | Deployment owner verifies a durable **cloud-backed** Client URL after recording/submission; no Mac-local backend, expiring Preview-only session or unreviewed protection bypass may stand in for judge access. Document the separate Vercel access gate and Floww app login for multiple judges without a shared Admin credential or public signer key. |
| Pending independent sessions | Using judge-like fresh sessions, confirm each judge signs in with their own identity and sees only their own Tasks; confirm Admin remains role-gated and no owner Task leaks. Test access after a fresh browser/session, not just the recording session. |
| Pending test funding | Public overview and B/C policy scenarios can be reviewed without chain funding, but an actual A wallet path needs test ETH for gas and Floww fixture fUSDC **per judge wallet**. The app does not provide a local faucet/burner balance. Deployment owner must supply a safe faucet or controlled test-funding source, exact instructions and per-wallet limits; opening the hosted link alone cannot pay. Never distribute a shared signer/private key. |
| Pending bounded capacity | Once the exact deployment is healthy, deployment owner may check read-only concurrency at 5 sessions, then 10 only if the first tier is healthy. Record latency/errors, deployment SHA and time; do not use payment, signing or Task creation as load probes. |
| Pending freeze/submission | Pin the exact Client/Admin/Server/Contract and hosted deployment SHAs; verify public links, viewer permission, final deck PDF (at most 10 pages), video, disclosure and release manifest. Submission owner records the final form/receipt and freeze point before calling this submission-ready. |
