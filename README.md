<div align="center">

# 🌊 Floww — Flow Wallet

### Bounded AI spending. Clear rules. Verifiable outcomes.

**The user sets the mandate. AI proposes. Deterministic checks enforce the scope.**

<p>
  <img src="https://img.shields.io/badge/AI%20Spending-Bounded-4261FF?style=for-the-badge" alt="Bounded AI spending" />
  <img src="https://img.shields.io/badge/Kiln-qwen3--32b-FFFF5C?style=for-the-badge&labelColor=333333" alt="Kiln qwen3-32b" />
  <img src="https://img.shields.io/badge/Status-Integration%20in%20progress-F1EDE2?style=for-the-badge&labelColor=333333" alt="Integration in progress" />
</p>

<em>Less autopilot. More intention. Let good decisions flow.</em>

</div>

---

## ✨ What is Floww?

Floww is a team project for bounded AI spending. The user confirms a spending mandate, AI proposes actions within that scope, and deterministic checks enforce the permitted limits.

This repository is the **integration and submission entry point** for the Floww project. The currently runnable server slice validates a confirmed mandate, fetches a server-owned test quote, executes a bounded model/tool conversation, and persists owner-only evidence.

The complete wallet-to-purchase experience is still being integrated. The current priority is to prove one core architecture journey—from an exact user-reviewed request to bounded execution and verifiable results.

> Broader consumer services and fiat funding remain longer-term product scope. Actual authentication, wallet authorization, and settlement still require integration.

## 🧭 Current integration priority

Follow the [core architecture demo handoff](docs/ARCHITECTURE_DEMO_HANDOFF.md) for the intended journey.

```mermaid
flowchart LR
    U[User-reviewed request] --> M[Confirmed mandate]
    M --> A[AI proposes an action]
    A --> P[Deterministic scope checks]
    P --> R[Reviewable result and evidence]
    P --> D[Blocked with a recorded reason]
    R -. wallet authorization and settlement still integrating .-> W[Verifiable purchase]
