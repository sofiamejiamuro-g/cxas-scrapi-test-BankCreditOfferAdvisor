# Technical Design Document (TDD): Bank Credit Offer Advisor & Closing Flow

> This is a **living document** -- update it whenever requirements, agent behavior, or evals change.
> Update the TDD first, then update evals to match.

## Agent Design

### Architecture
- **Modality**: Chat / Text-only (`gemini-3-flash`)
- **Root Agent (`credit_advisor_agent`)**: Explains credit offer terms, negotiates terms, and logs declination reasons. Upon offer acceptance, transfers to `closing_agent`.
- **Sub-Agent (`closing_agent`)**: Handles closing requirements once an offer is accepted: prompts customer to upload verification documents and schedule an in-person signature date at bank offices.

### Tools
| Tool Name | Type | Purpose |
|-----------|------|---------|
| `get_credit_offer` | API connector | Retrieves active credit offer terms (amount, rate, term length, monthly payment) |
| `evaluate_negotiation` | API connector | Checks if requested adjustment is eligible |
| `accept_credit_offer` | API connector | Confirms offer acceptance |
| `log_declination_reason` | API connector | Records declination reason |
| `set_session_state` | Python function | Tracks session progression |
| `upload_document` | API connector | Accepts customer identity/income document payloads |
| `schedule_signature` | API connector | Books an in-person appointment at bank offices for signing |

### Routing Logic
- **Acceptance Routing**: Once the customer explicitly accepts the credit offer in `credit_advisor_agent`, transfer to `closing_agent`.
- **Multilingual Switching**: Explicit switching between English (`en`), Spanish (`es`), and Portuguese (`pt`).

### Variables
| Variable | Source | Notes |
|----------|--------|-------|
| `customer_id` | Session parameter | Provided by banking platform |
| `offer_id` | Session parameter | Provided by banking platform |
| `decision_status` | Derived in before_agent_callback | Tracks ACCEPTED, DECLINED, NEGOTIATING |

### Callbacks
| Callback | Agent | Purpose |
|----------|-------|---------|
| `before_agent` | `credit_advisor_agent` | Initializes decision_status and customer offer context |

---

## Eval Design

### Coverage Map
| Requirement | Eval Type | Rationale | Priority | Severity | Tags |
|-------------|-----------|-----------|----------|----------|------|
| Review Credit Offer | Golden | Deterministic offer retrieval | P0 | NO-GO | `review` |
| Negotiate Terms | Sim | Dynamic negotiation boundaries | P1 | HIGH | `negotiate` |
| Accept & Transfer | Golden | Deterministic transfer to closing_agent | P0 | NO-GO | `transfer, closing` |
| Document Upload & Schedule | Sim | Interactive closing document upload & appointment booking | P0 | NO-GO | `closing, onboarding` |
| Decline Offer | Golden | Deterministic declination logging | P0 | NO-GO | `decline` |

### Golden vs Sim Decision
- **Use goldens** for deterministic offer reviews, declination logging, and multi-agent transfers.
- **Use sims** for dynamic multi-step closing document collection and date scheduling.

### Test Data (Customer Profiles)
| Profile | customer_id | offer_id | Scenario |
|---------|-------------|----------|----------|
| Standard Offer | `CUST-88192` | `OFFER-101` | Active $10,000 personal loan offer |

---

## Tracking

### Pass Rate History
| Date | Goldens | Sims | Tool Tests | Callback Tests | Notes |
|------|---------|------|------------|----------------|-------|
| 2026-06-13 | 0/0 | 0/0 | 0/0 | 0/0 | Closing flow update |

### Known Issues
- (none)

### Changelog
| Date | Change | Author |
|------|--------|--------|
| 2026-06-13 | Added closing_agent subagent architecture & tools | Antigravity |
