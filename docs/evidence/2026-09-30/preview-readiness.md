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

## Later release and controller observations — 10:39–10:57 KST

These later facts update the release snapshot; they do not rewrite the 09:04–09:45 observations above. The deployed-source facts below come from the controller's dated `control/F037_DEPLOY_READINESS_20260930.md` record. The hosted OTP/login observation was reported by the controller during F046; no raw OTP, session, signature, browser trace or external acceptance artifact was added to this public file.

| Surface | Source / observed result / remaining boundary |
| --- | --- |
| Client release source | [PR #10](https://github.com/web5five/Floww_Frontend_Client/pull/10) merged as `5be68d257d979a313ec7f4303bef49b481ada270`; [PR #11](https://github.com/web5five/Floww_Frontend_Client/pull/11) merged as current Client main `7a00a6ef6e9a04cf0987b22c2a53e4d3bb98b76d` (GitHub main/PR checked 10:57 KST). Product Magic is therefore merged source, not an unmerged follow-up. |
| Client protected Preview deployment | Controller's F037 record says PR11 source was deployed READY as `dpl_GLSnHnUX7pXKRn7ufjSa5qM5zbom` and the stable alias `https://floww-client-demo-preview-geond.vercel.app` was reassigned to it. The alias requires the approved Vercel share link or account permission; the plain URL redirects to Vercel access. The unique deployment URL is not the approved Magic/SIWE origin. |
| Hosted Magic login slice | Controller reported completion on that stable protected alias of Magic email OTP, a Sepolia wallet, exact SIWE/server login, and arrival at `/pharmacy` with public wallet address `0x4B03f3eD55Ae3912f318D5746B45478ED467faa8`. This is a human-operated hosted browser observation, not a spend signature, purchase, or independent artifact replay. The address identifies this login observation; it is not the scripted F031 payment owner/TaskAccount. No email or OTP is published. |
| Admin release source | [PR #8](https://github.com/web5five/Floww_Frontend_Admin/pull/8) merged as current Admin main `d64468b817023a8bddace22676b36cab85b32d30` (GitHub main/PR checked 10:57 KST). F037 records an earlier READY Admin Production UI at `https://floww-admin-demo.vercel.app` from PR #7/main `50b4b2eaa3a2fd5d5ba96db6ff0cbb0848fa3f15`, plus successful ADMIN API/BFF authentication. PR #8 deployment and authenticated **browser** audit on its artifact are not established here. |
| Backend and contract | GitHub Server main remains `153b5f3e78467f1dc5cbc8d58d9c86ee52aaf8c6`, Contract main remains `d4e6a7d7b7635634b8a59f7c87bba91d3b311f9d` (checked 10:57 KST). F037 records Backend Production health/Admin at `https://floww-server-demo.vercel.app`, with full wallet/Kiln/Sepolia execution settings Preview-only. No new hosted purchase is inferred. |

**Still open:** current hosted Pharmacy A success and B/C denial completion, same-Task Client/Admin browser audit, refresh/reconnect recovery, actual hosted payment/fulfillment, and separate final video/deck/submission artifacts. A displayed pharmacy route or wallet identity grants no purchase authority. The independently checked payment remains the **older local-backend + scripted-owner + public-Sepolia** F031 run at Server runtime `e86e3592eeed512d4f41601a1a46108d45472a39`, executable JAR SHA-256 `cc58571cbe975afb7ad1335909b4a81b925c7d88925aaf4c1482c696cae7d7a2`, and Contract source `d4e6a7d7b7635634b8a59f7c87bba91d3b311f9d`; see the [independent report](https://github.com/web5five/Floww_Server/blob/6f1d3029885808bd35d706b47688b24166ed9273/docs/F031_INDEPENDENT_SEPOLIA.md). It does not establish payment from the hosted Magic owner. This public record is an evidence summary, not a final submission receipt.
