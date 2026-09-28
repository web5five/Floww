# 2026-09-29 module verification / 모듈 검증

The visible Orca GPT-6 Sol session implemented the Java server; the controller separately tested the packaged artifact. [verification.json](verification.json) records the JAR SHA-256, checks, policy rejections, and sanitized live-model metadata. Source revision is pinned in the hub release manifest after publication.

- Java tests: **13**, zero failures/errors (real PostgreSQL and HTTP fixtures).
- Independent black-box checks: **82 assertions across 15 fixture scenarios**, including final-call quote/mandate expiry, owner isolation, concurrent claims, replay, history, provenance and incomplete retry usage.
- Docker: **7 checks passed**; UID 10001, host loopback only, real DB, anonymous denial and missing integration fail-closed. The first startup probe was too short under local load; increasing only the startup allowance from 30 to 120 seconds allowed the same artifact to start. Business-operation limits were unchanged.
- Final live Kiln: **4 model calls, 3 matched tool/result pairs, 3,021 reported tokens** using `qwen3-32b`; generation IDs are in the JSON. The merchant remained a local HTTP fixture.
- Execution: `7c92f21b-ffca-4a9e-beca-51b833faa1db`; status `REVIEWED`, meaning quote ready for human review. This is not a purchase, wallet approval, payment or fulfillment result.

13개 Java 테스트, 별도 API 검사 82개, Docker 검사 7개를 통과했습니다. 최종 실행 파일로 실제 Kiln 도구 왕복 3회와 사용량을 확인했습니다. 판매자는 로컬 테스트 서버이며 실제 거래·인간 승인·전체 제품 인수는 아직 증명하지 않습니다.

Reproduce the local independent checks using [runtime readiness](../../RUNTIME_READINESS.md) and `scripts/verify_server.py`. The app uses test-only development identities. Core auth/migrations/recovery, real merchant, wallet settlement, UI integration, video and deck remain separate gates. Full release validation is expected to fail until they are supplied and reviewed.

Verified server source: [3f1fe3e228f2e6b151d56f2ac7d99efbae7704d2](https://github.com/web5five/Floww_Server/commit/3f1fe3e228f2e6b151d56f2ac7d99efbae7704d2). Controller, container and final live checks used the same packaged JAR hash in the JSON.
