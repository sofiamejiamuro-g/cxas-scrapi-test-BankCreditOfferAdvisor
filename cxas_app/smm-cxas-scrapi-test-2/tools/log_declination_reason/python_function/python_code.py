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
log_declination_reason — Declination Logging Tool
"""


def log_declination_reason(
    offer_id: str = "", customer_id: str = "", reason: str = ""
) -> dict:
    """Record customer decision to decline a credit offer.

    Args:
        offer_id: The credit offer ID.
        customer_id: The customer ID.
        reason: Primary reason for declining (e.g., 'rate_too_high',
          'not_needed').

    Returns:
        dict: Declination logging confirmation.
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
        "log_id": f"DECL-{offer_id}-8821",
        "recorded_reason": reason or "unspecified",
        "disposition": "OFFER_DECLINED",
    }
