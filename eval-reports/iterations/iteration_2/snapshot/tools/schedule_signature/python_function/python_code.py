def schedule_signature(preferred_date: str = "2026-06-20", preferred_time: str = "10:00 AM", office_location: str = "Main Branch") -> str:
    """Schedules an in-person appointment for final signing at bank offices.

    Args:
        preferred_date: Requested appointment date.
        preferred_time: Requested appointment time.
        office_location: Bank office location.

    Returns:
        JSON string confirming scheduled signing date.
    """
    import json
    try:
        if not preferred_date:
            return json.dumps({
                "status": "error",
                "error": "Preferred date is required.",
                "agent_action": "Ask the customer for their preferred signing date."
            })
        return json.dumps({
            "status": "SCHEDULED",
            "appointment_id": "APT-88291",
            "date": preferred_date,
            "time": preferred_time,
            "location": office_location,
            "message": f"Signature appointment confirmed for {preferred_date} at {preferred_time}."
        })
    except Exception as e:
        return json.dumps({
            "status": "error",
            "error": f"Scheduling failed: {str(e)}",
            "agent_action": "Inform the customer that appointment scheduling failed and offer assistance."
        })
