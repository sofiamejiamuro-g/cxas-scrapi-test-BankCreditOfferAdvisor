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
accept_credit_offer — Offer Acceptance Tool
"""


def accept_credit_offer(offer_id: str = "", customer_id: str = "") -> dict:
    """Confirm acceptance of a credit offer and trigger disbursement.

    Args:
        offer_id: The credit offer ID.
        customer_id: The customer ID.

    Returns:
        dict: Acceptance confirmation details including disbursement status.
    """
    if not offer_id or not customer_id:
        return {
            "status": "error",
            "error": "offer_id and customer_id are required.",
            "agent_action": (
                "Ask the customer to confirm their identifier or offer code."
            ),
        }

    return {
        "status": "success",
        "confirmation_code": f"DISB-{offer_id}-9912",
        "disbursement_status": "SCHEDULED",
        "next_steps": (
            "Funds will be deposited into the primary linked account within 1-2"
            " business days."
        ),
    }
