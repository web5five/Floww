# Runtime readiness / 실행 환경 준비 현황

Snapshot: 2026-09-29 KST. A component foundation is not an application build. Use the immutable revisions and evidence linked by the release manifest.

## Verified or prepared / 확인한 기반

| Item / 항목 | State / 상태 |
| --- | --- |
| Java server | Java 21, Spring Boot 3.5.16, PostgreSQL 16.4; Maven Wrapper 3.9.16 with distribution checksum / 버전 고정 및 실제 실행 검증 대상 |
| Dependency management | Spring Boot parent/BOM and Maven Wrapper control resolved versions; Maven is not an npm lockfile workflow / BOM·Wrapper 관리 |
| Database | Loopback-published Postgres with healthcheck and persistent volume; preserve shared data / DB 상태 검사·데이터 보존 |
| Secrets | Placeholder-only env example; local credentials excluded; narrow Docker context / 예시 환경 파일·비밀정보 제외 |
| Container | Runtime JRE image, non-root UID, internal container binding and loopback host publication / 비루트 실행·포트 경계 |
| CI | Hub manifest check and server PostgreSQL integration check; observed runs linked in PRs / 실제 검사 결과는 PR 확인 |
| Client/Admin/Contracts | Shared instructions and issue/PR templates only; application versions, lockfiles, runtime images and CI must follow actual implementation / 앱 구성은 담당 구현 이후 |

The server's startup SQL is a provisional initializer, not a versioned migration strategy. Development bearer tokens, synchronous execution and crash recovery need core-backend review before shared deployment. A healthy process is not a reachable merchant, funded wallet or verified payment.

서버의 인증·마이그레이션·작업 복구·배포 경계를 코어 담당자와 검토해야 합니다. 앱이 없는 저장소에 의미 없는 의존성·도커·CI를 넣지 않았으며, 구현 착수 시 아래 기준을 적용합니다.

## Before each component's first implementation PR / 첫 구현 PR 기준

1. Select and pin the supported runtime and package manager. Commit the appropriate dependency lockfile or build wrapper. Keep runtime secrets server-side.
2. Provide an env example, a reproducible clean-checkout command and a health/readiness distinction. Document local ports and how to stop only the processes started.
3. Add meaningful CI for the real implementation. Test with actual persistence where behavior depends on it; do not substitute a green placeholder job.
4. Document authentication, schema/migration ownership, amount units, error/status contracts, idempotency and evidence provenance.
5. Verify the published container or deployment separately. Record exact component SHAs, checks, known limits and independent reviewer.

Redis, pgvector, Kafka, Eureka, Config Server, browser sandbox and a separate Python service remain deferred. Adding one requires a concrete problem, owner and operating cost; repository existence alone is not a reason.


## Independent server check / 독립 서버 검증

After building the server JAR using its runbook and starting the local `floww_server-db-1` PostgreSQL container, run from this hub checkout:

```sh
export FLOWW_SERVER_PATH=/absolute/path/to/Floww_Server
# JAVA_HOME must point to your Java 21 JDK.
python3 scripts/verify_server.py
```

This starts its own app on loopback port 18085 and HTTP fixtures on 18998/18999, uses random development tokens, creates a separate audit database in the existing PostgreSQL container (port 55433), then stops its own processes. It uses no real Kiln key or payment. Keep those ports free. Sanitized reports remain under ignored `.local/controller-verification`; the database is retained for inspection. Do not run it against a production/shared deployment. Set up the server's ignored `.env` first as documented; no credential values are printed by this harness.

이 검사는 구현자의 테스트와 별도로 작성한 API 검증입니다. 새 감사용 DB를 만들며 기존 DB를 지우지 않습니다. PostgreSQL 컨테이너명·포트는 위 로컬 실행 구성 기준입니다.
