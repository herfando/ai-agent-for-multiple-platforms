from fastapi import APIRouter, Request
from app.services.webhook_service import push_message

router = APIRouter()


# =========================
# VERIFY WEBHOOK (optional)
# Telegram sebenarnya tidak pakai verify seperti Meta
# =========================
@router.get("/telegram")
def verify():
    return "OK"


# =========================
# RECEIVE MESSAGE (POST)
# =========================
@router.post("/telegram")
async def receive(request: Request):

    data = await request.json()

    print("TELEGRAM WEBHOOK:", data)

    try:
        message = data["message"]

        sender_id = str(message["chat"]["id"])
        text = message.get("text", "")

        push_message(sender_id, text, "telegram")

        return {"status": "queued"}

    except Exception as e:
        print("Telegram webhook error:", str(e))
        return {"status": "ignored"}