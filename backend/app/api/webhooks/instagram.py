from fastapi import APIRouter, Request
from app.services.webhook_service import push_message

router = APIRouter()

# =========================
# VERIFY WEBHOOK (GET)
# =========================
@router.get("/instagram")
def verify(
    hub_mode: str = None,
    hub_challenge: str = None,
    hub_verify_token: str = None
):

    VERIFY_TOKEN = "my_verify_token"

    if hub_verify_token == VERIFY_TOKEN:
        return int(hub_challenge)

    return {"error": "invalid token"}


# =========================
# RECEIVE MESSAGE (POST)
# =========================
@router.post("/instagram")
async def receive(request: Request):

    data = await request.json()

    print("INSTAGRAM WEBHOOK:", data)

    try:
        entry = data["entry"][0]
        messaging = entry["messaging"][0]

        sender_id = messaging["sender"]["id"]
        text = messaging["message"]["text"]

        push_message(sender_id, text, "instagram")

        return {"status": "queued"}

    except Exception as e:
        print("Instagram webhook error:", str(e))
        return {"status": "ignored"}