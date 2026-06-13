# Product Requirements Document (PRD): Bank Credit Offer Advisor

## 1. Overview
The Bank Credit Offer Advisor is a chat-based conversational agent designed to guide bank customers through reviewing, negotiating, accepting, or declining credit offers.

## 2. Core Capabilities & Intents
- **Review Credit Offer**: Retrieve and explain the terms of an active credit offer (amount, interest rate, term length, monthly payment).
- **Negotiate Terms**: Evaluate requested adjustments (e.g., higher credit limit, lower interest rate, longer repayment term) against eligibility criteria.
- **Accept Offer**: Confirm acceptance of the credit offer and initiate onboarding/disbursement.
- **Decline Offer**: Log rejection of the credit offer and record the customer's primary reason.

## 3. Modality & Model Settings
- **Modality**: Chat / Text-only
- **Model**: `gemini-3-flash`

## 4. Multilingual Support
- **Supported Languages**: English (`en`), Spanish (`es`), Portuguese (`pt`)
- **Switching Mode**: Explicit switching (e.g., "Speak in Spanish").
