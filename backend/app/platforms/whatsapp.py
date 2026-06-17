import requests

TOKEN = "WHATSAPP_TOKEN"
PHONE_NUMBER_ID = "YOUR_PHONE_ID"


def send_whatsapp(number, message):

    url = f"https://graph.facebook.com/v18.0/{PHONE_NUMBER_ID}/messages"

    payload = {
        "messaging_product": "whatsapp",
        "to": number,
        "type": "text",
        "text": {"body": message}
    }

    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json"
    }

    res = requests.post(url, json=payload, headers=headers)

    print("WA RESPONSE:", res.json())

    return res.json()