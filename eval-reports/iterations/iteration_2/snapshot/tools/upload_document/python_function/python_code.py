def upload_document(document_type: str = "identity_verification", file_name: str = "doc.pdf") -> str:
    """Uploads verification documentation required for loan closing.

    Args:
        document_type: Type of document being uploaded.
        file_name: Name of the uploaded file.

    Returns:
        JSON string confirming document receipt.
    """
    import json
    try:
        if not file_name:
            return json.dumps({
                "status": "error",
                "error": "File name is required.",
                "agent_action": "Ask the customer to provide the document file."
            })
        return json.dumps({
            "status": "UPLOADED",
            "document_type": document_type,
            "verification_id": "VERIF-33881",
            "message": "Document uploaded and validated successfully."
        })
    except Exception as e:
        return json.dumps({
            "status": "error",
            "error": f"Upload failed: {str(e)}",
            "agent_action": "Inform the customer that document upload failed and offer support."
        })
