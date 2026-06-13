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
get_credit_offer — Credit Offer Retrieval Tool
"""


def get_credit_offer(offer_id: str = "", customer_id: str = "") -> dict:
    """Retrieve active credit offer terms for a customer.

    Args:
        offer_id: The credit offer ID.
        customer_id: The customer ID.

    Returns:
        dict: Offer terms including amount, interest rate, term length, and monthly payment.
    """
    if not offer_id or not customer_id:
        return {
            "status": "error",
            "error": "offer_id and customer_id are required.",
            "agent_action": "Ask the customer to confirm their identifier or offer code.",
        }

    if offer_id == "OFFER-202":
        return {
            "status": "success",
            "offer": {
                "offer_id": offer_id,
                "customer_id": customer_id,
                "amount": "$25,000",
                "interest_rate": "6.5%",
                "term_length": "48 months",
                "monthly_payment": "$592.00",
                "negotiable": True,
            },
        }

    return {
        "status": "success",
        "offer": {
            "offer_id": offer_id,
            "customer_id": customer_id,
            "amount": "$10,000",
            "interest_rate": "8.5%",
            "term_length": "36 months",
            "monthly_payment": "$315.00",
            "negotiable": False,
        },
    }
