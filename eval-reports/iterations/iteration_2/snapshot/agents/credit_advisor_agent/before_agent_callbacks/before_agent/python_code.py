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
before_agent_callback — credit_advisor_agent

PURPOSE:
    Initializes decision_status and customer offer context when customer_id
    and offer_id are provided as session parameters.
"""

from typing import Optional


def before_agent_callback(callback_context: CallbackContext) -> Optional[Content]:
    state = callback_context.state

    if state.get("decision_status"):
        return None

    customer_id = state.get("customer_id", "")
    offer_id = state.get("offer_id", "")

    if customer_id and offer_id:
        state["decision_status"] = "REVIEWING"

    return None
