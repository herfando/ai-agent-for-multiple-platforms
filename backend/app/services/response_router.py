from app.platforms.instagram import send_instagram
from app.platforms.whatsapp import send_whatsapp


def route_response(platform: str, response: dict, user_id: str):

    message = response["message"]

    if platform == "instagram":
        return send_instagram(user_id, message)

    if platform == "whatsapp":
        return send_whatsapp(user_id, message)

    print("UNKNOWN PLATFORM")