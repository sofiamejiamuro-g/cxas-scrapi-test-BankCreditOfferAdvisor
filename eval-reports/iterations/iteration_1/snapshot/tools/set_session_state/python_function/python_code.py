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
set_session_state — Session State Tracking Tool
"""


def set_session_state(
    decision_status: str = "", negotiation_milestone: str = ""
) -> dict:
    """Write decision and negotiation state variables to session state.

    Args:
        decision_status: Offer decision status (e.g., 'ACCEPTED', 'DECLINED',
          'NEGOTIATING').
        negotiation_milestone: Current milestone in negotiation.

    Returns:
        dict: Status of updated state variables.
    """
    updated = {}
    if decision_status:
        context.state["decision_status"] = decision_status
        updated["decision_status"] = decision_status
    if negotiation_milestone:
        context.state["negotiation_milestone"] = negotiation_milestone
        updated["negotiation_milestone"] = negotiation_milestone

    if not updated:
        return {
            "agent_action": (
                "Provide at least one parameter to update session state."
            )
        }

    return {
        "status": "success",
        "updated_variables": updated,
    }
