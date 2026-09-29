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
