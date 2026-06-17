def build_response(ai_text: str):

    return {
        "message": ai_text,
        "type": "text",
        "timestamp": None
    }