from fastapi import APIRouter, Request
import os

router = APIRouter()

META_APP_ID = os.getenv("META_APP_ID")
META_REDIRECT_URI = os.getenv("META_REDIRECT_URI")

# 1. CONNECT (redirect ke Facebook login)
@router.get("/connect")
def connect():
    print("APP ID:", META_APP_ID)
    print("REDIRECT:", META_REDIRECT_URI)
    url = (
        "https://www.facebook.com/v20.0/dialog/oauth"
        f"?client_id={META_APP_ID}"
        f"&redirect_uri={META_REDIRECT_URI}"
        "&scope=pages_show_list,instagram_basic,instagram_manage_messages"
        "&response_type=code"
    )
    return {"url": url}


# 2. CALLBACK (terima code dari Meta)
@router.get("/callback")
def callback(request: Request):
    code = request.query_params.get("code")
    return {"code": code}