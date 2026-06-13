# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
evaluate_negotiation — Negotiation Evaluation Tool
"""


def evaluate_negotiation(
    offer_id: str = "", requested_rate: str = "", requested_amount: str = "", requested_term: str = ""
) -> dict:
    """Evaluate if requested credit offer adjustments are eligible.

    Args:
        offer_id: The credit offer ID.
        requested_rate: Requested interest rate (e.g., '6.0%').
        requested_amount: Requested loan amount (e.g., '$30,000').
        requested_term: Requested repayment term length (e.g., '48 months').

    Returns:
        dict: Evaluation result indicating approval eligibility and updated terms.
    """
    if not offer_id:
        return {
            "status": "error",
            "error": "offer_id is required.",
            "agent_action": "Ask the customer to clarify which offer they are negotiating.",
        }

    return {
        "status": "success",
        "eligible": True,
        "adjusted_offer": {
            "offer_id": offer_id,
            "amount": requested_amount or "$25,000",
            "interest_rate": requested_rate or "6.0%",
            "term_length": requested_term or "48 months",
            "monthly_payment": "$578.00",
        },
        "note": "Adjustment pre-approved based on credit profile.",
    }
