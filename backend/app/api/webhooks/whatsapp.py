from fastapi import APIRouter, Request
from app.services.webhook_service import push_message

router = APIRouter()

@router.get("/whatsapp")
def verify():
    return "OK"


@router.post("/whatsapp")
async def receive(request: Request):

    data = await request.json()

    print("WHATSAPP WEBHOOK:", data)

    try:
        message = data["entry"][0]["changes"][0]["value"]["messages"][0]

        sender = message["from"]
        text = message["text"]["body"]

        push_message(sender, text, "whatsapp")

        return {"status": "queued"}
        

    except Exception as e:
        print("WhatsApp webhook error:", str(e))
        return {"status": "ignored"}