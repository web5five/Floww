# Hosted readiness observation — September 30, 2026 KST

This is a sanitized controller/deployment-owner observation, not a raw provider log or complete user acceptance. The observations below were recorded at 09:04–09:45 KST. Newer deployments must be checked separately.

| Surface | Source / observed result |
| --- | --- |
| Client protected Preview | Source `5003d0a49d3a6c46c1055b178a722e9815f37ad7`, deployment `dpl_DnQe8tHxdunajREd1a4CPYgrV2fn`, stable alias `https://floww-client-demo-preview-geond.vercel.app`. Normal unauthenticated access returns the Vercel access flow. |
| Wallet configuration | `GET /api/wallet-auth/config` returned enabled, `team-jwt`, business-ready and Sepolia chain11155111. |
| Wallet backend readiness | `GET /api/wallet-auth/health` returned ready through the server-only protected backend connection. |
| Login challenge | A disposable nonce request produced the exact stable Client Preview origin. No wallet signature was claimed by this check. |
| Anonymous business boundary | Task and voice routes returned401 with no-store. |
| Visible Client | Controller independently opened the protected Preview in the in-app browser, checked the Overview/brand/wallet picker and login redirect before scenario access. |
| Admin | Source `74fe6f40c263735c7cfb705eccb447e2c88bfbfb` at `https://floww-admin-demo.vercel.app`: login200, icon200, anonymous audit401. An actual ADMIN login was not performed; operator provisioning remains separate. |

No share-link token, bypass secret, session cookie, nonce value, email, password, wallet signature or private key is recorded here. HTTP readiness is not payment readiness. These observations do not establish Magic OTP, real wallet login, live voice conversation, same-Task Admin audit or a full current hosted purchase. Later Client PR10/source `5be68d257d979a313ec7f4303bef49b481ada270` is merged, but its deployment/acceptance must not be attributed to the earlier check above.
