# Technical Design Document (TDD): Bank Credit Offer Advisor

> This is a **living document** -- update it whenever requirements, agent behavior, or evals change.
> Update the TDD first, then update evals to match.

## Agent Design

### Architecture
- **Modality**: Chat / Text-only (`gemini-3-flash`)
- **Root Agent (`credit_advisor_agent`)**: Handles explaining the credit offer terms, evaluating negotiation requests, confirming acceptance, or logging declination reasons.

### Tools
| Tool Name | Type | Purpose |
|-----------|------|---------|
| `get_credit_offer` | API connector | Retrieves the customer's active credit offer terms (amount, rate, term length, monthly payment) |
| `evaluate_negotiation` | API connector | Checks if requested adjustment (e.g., lower rate, higher amount) is pre-approved or eligible |
| `accept_credit_offer` | API connector | Confirms offer acceptance and triggers bank disbursement |
| `log_declination_reason` | API connector | Records the customer's decision to decline and their primary reason |
| `set_session_state` | Python function | Internal state tracker for negotiation and decision milestones |

### Routing Logic
- Single-agent chat advisor flow.
- Explicit language switching ("Speak in Spanish", "Fale em português").

### Variables
| Variable | Source | Notes |
|----------|--------|-------|
| `customer_id` | Session parameter | Provided by banking platform |
| `offer_id` | Session parameter | Provided by banking platform |
| `decision_status` | Derived in before_agent_callback | Default empty; tracks ACCEPTED, DECLINED, NEGOTIATING |

### Callbacks
| Callback | Agent | Purpose |
|----------|-------|---------|
| `before_agent` | `credit_advisor_agent` | Initializes decision_status and customer offer context |

---

## Eval Design

### Coverage Map
| Requirement | Eval Type | Rationale | Priority | Severity | Tags |
|-------------|-----------|-----------|----------|----------|------|
| Review Credit Offer | Golden | Deterministic offer retrieval & explanation | P0 | NO-GO | `review, credit-offer` |
| Negotiate Terms | Sim | Negotiation dialogue & constraint checking | P1 | HIGH | `negotiate, terms` |
| Accept Offer | Golden | Deterministic acceptance confirmation & disbursement | P0 | NO-GO | `accept, onboarding` |
| Decline Offer | Golden | Deterministic declination logging with reason | P0 | NO-GO | `decline, reason` |

### Golden vs Sim Decision
- **Use goldens** when reviewing fixed offer terms, confirming acceptance, or logging declination reasons.
- **Use sims** for negotiation where user requests vary and agent evaluates dynamic boundaries.

### Test Data (Customer Profiles)
| Profile | customer_id | offer_id | Scenario |
|---------|-------------|----------|----------|
| Standard Offer | `CUST-88192` | `OFFER-101` | Active $10,000 personal loan offer |
| High-Tier Offer | `CUST-99201` | `OFFER-202` | Negotiable premium credit offer |

---

## Build Steps

1. Create app and root agent (`credit_advisor_agent`) with comprehensive instructions.
2. Create tools (`get_credit_offer`, `evaluate_negotiation`, `accept_credit_offer`, `log_declination_reason`, `set_session_state`).
3. Define session parameters (`customer_id`, `offer_id`) and derived variables (`decision_status`).
4. Implement callback (`before_agent`).
5. Write golden evaluation YAML files.
6. Write simulation evaluation YAML entries.
7. Run evaluation validation and verify zero warnings/errors.

---

## Pass Rate History

| Date | Goldens | Sims | Tool Tests | Callback Tests | Notes |
|------|---------|------|------------|----------------|-------|
| 2026-06-13 | 0/0 | 0/0 | 0/0 | 0/0 | Initial draft |

---

## Known Issues

- (none)

---

## Changelog

| Date | Change | Author |
|------|--------|--------|
| 2026-06-13 | Initial TDD created from PRD | Antigravity |
