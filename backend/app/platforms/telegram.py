from fastapi import APIRouter, Request

router = APIRouter()

@router.post("/telegram")
async def telegram_webhook(request: Request):

    data = await request.json()

    print("TELEGRAM WEBHOOK:", data)

    try:
        message = data["message"]
        sender = str(message["from"]["id"])
        text = message["text"]

        return {
            "conversation_id": sender,
            "content": text,
            "platform": "telegram"
        }

    except:
        return {"status": "ignored"}