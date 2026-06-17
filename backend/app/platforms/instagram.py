import requests

ACCESS_TOKEN = "META_ACCESS_TOKEN"


def send_instagram(user_id, message):

    url = "https://graph.facebook.com/v18.0/me/messages"

    payload = {
        "recipient": {"id": user_id},
        "message": {"text": message}
    }

    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }

    res = requests.post(url, json=payload, headers=headers)

    print("IG RESPONSE:", res.json())

    return res.json()