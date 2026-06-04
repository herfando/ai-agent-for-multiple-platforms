def detect_intent(message: str):

    msg = message.lower()

    if any(x in msg for x in ["harga", "berapa", "price"]):
        return "pricing"

    if any(x in msg for x in ["stok", "ada", "available"]):
        return "availability"

    if any(x in msg for x in ["beli", "order", "checkout"]):
        return "buying"

    if any(x in msg for x in ["komplain", "rusak", "jelek"]):
        return "complaint"

    return "general"