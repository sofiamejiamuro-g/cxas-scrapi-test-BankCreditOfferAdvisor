# Technical Design Document (TDD): Bank Credit Offer Advisor & Negotiation Flow

> This is a **living document** -- update it whenever requirements, agent behavior, or evals change.
> Update the TDD first, then update evals to match.

## Agent Design

### Architecture
- **Modality**: Chat / Text-only (`gemini-3-flash`)
- **Root Agent (`credit_advisor_agent`)**: Explains credit offer terms and logs declination reasons. Transfers to `negotiation_agent` upon negotiation requests, and transfers to `closing_agent` upon offer acceptance.
- **Sub-Agent (`negotiation_agent`)**: Dedicated underwriting negotiation specialist. Evaluates requested loan amount and repayment term length adjustments against bank eligibility thresholds.
- **Sub-Agent (`closing_agent`)**: Guides accepted customers to upload verification documents and schedule signing at bank offices.

### Tools
| Tool Name | Type | Purpose |
|-----------|------|---------|
| `get_credit_offer` | API connector | Retrieves active credit offer terms (amount, rate, term length, monthly payment) |
| `evaluate_negotiation` | API connector | Checks if requested adjustment (amount, rate, term) is eligible |
| `accept_credit_offer` | API connector | Confirms offer acceptance |
| `log_declination_reason` | API connector | Records declination reason |
| `set_session_state` | Python function | Tracks session progression |
| `upload_document` | API connector | Accepts verification documents |
| `schedule_signature` | API connector | Books an in-person signing appointment at bank offices |

### Routing Logic
- **Negotiation Routing**: When the customer asks to negotiate or adjust offer amount or repayment term, transfer to `negotiation_agent`.
- **Acceptance Routing**: Once accepted, transfer to `closing_agent`.
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
| Transfer to Negotiation | Golden | Deterministic transfer to negotiation_agent | P0 | NO-GO | `transfer, negotiate` |
| Negotiate Amount & Term | Sim | Dynamic boundary evaluation in negotiation_agent | P0 | HIGH | `negotiate, underwriting` |
| Accept & Transfer | Golden | Deterministic transfer to closing_agent | P0 | NO-GO | `transfer, closing` |
| Document Upload & Schedule | Sim | Interactive closing document upload & appointment booking | P0 | NO-GO | `closing` |
| Decline Offer | Golden | Deterministic declination logging | P0 | NO-GO | `decline` |

### Golden vs Sim Decision
- **Use goldens** for multi-agent transfers, offer reviews, and declination logging.
- **Use sims** for dynamic multi-step closing workflows and negotiation boundary checking.

### Test Data (Customer Profiles)
| Profile | customer_id | offer_id | Scenario |
|---------|-------------|----------|----------|
| Standard Offer | `CUST-88192` | `OFFER-101` | Active $10,000 personal loan offer |

---

## Tracking

### Pass Rate History
| Date | Goldens | Sims | Tool Tests | Callback Tests | Notes |
|------|---------|------|------------|----------------|-------|
| 2026-06-13 | 0/0 | 0/0 | 0/0 | 0/0 | Negotiation sub-agent update |

### Known Issues
- (none)

### Changelog
| Date | Change | Author |
|------|--------|--------|
| 2026-06-13 | Added negotiation_agent subagent architecture & transfer rules | Antigravity |
