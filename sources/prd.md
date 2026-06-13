# Product Requirements Document (PRD): Bank Credit Offer Advisor, Negotiation & Closing Assistant

## 1. Overview
The Bank Credit Offer Advisor is a multi-agent conversational AI chat assistant built on GECX using **CXAS-scrapi**. It guides bank customers through reviewing pre-approved credit offers, negotiating amount and term length via a dedicated underwriting specialist, accepting offers, and completing closing verification workflows.

## 2. Core Capabilities & Multi-Agent Flow

### Phase 1: Credit Offer Advisory (`credit_advisor_agent`)
- **Review Credit Offer**: Retrieve and explain the customer's active credit offer terms (loan amount, interest rate, repayment term, monthly payment).
- **Transfer to Negotiation**: Route customers seeking to adjust loan amount or repayment term length to the Underwriting Negotiation Specialist.
- **Accept Offer**: Confirm customer acceptance of the credit offer and automatically transfer to the Closing Specialist.
- **Decline Offer**: Log offer rejection and record the customer's primary reason.

### Phase 2: Underwriting Negotiation (`negotiation_agent`)
- **Evaluate Requested Terms**: Partner with the customer to evaluate requested loan amount and repayment term length adjustments against underwriting boundaries via `evaluate_negotiation`.

### Phase 3: Closing & Onboarding (`closing_agent`)
- **Document Collection**: Guide accepted customers to submit required verification documentation (such as proof of identity or income) via `upload_document`.
- **In-Person Appointment Scheduling**: Prompt the customer to select a preferred date and time for final signature at bank offices via `schedule_signature`.

## 3. Modality & Model Settings
- **Modality**: Chat / Text-only
- **Model**: `gemini-3-flash` (or `gemini-3.1-flash-live`)

## 4. Multilingual Support
- **Supported Languages**: English (`en`), Spanish (`es`), Portuguese (`pt`)
- **Switching Mode**: Explicit switching (e.g., "Speak in Spanish" / "Fale em português").
