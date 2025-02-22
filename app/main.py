from fastapi import FastAPI, HTTPException
from app.email_utils import send_greeting_email
from app.config import settings
import uvicorn

app = FastAPI()

@app.get("/")
def home():
    msg = {
        "message": "FastAPI Email Sender is Running!",
        "note": "This version is commited by Gokul Branch user!",
        "time": "7:52 PM" 
    }
    return msg

@app.post("/send-email/")
def send_email(recipients: list[str]):
    try:
        send_greeting_email(recipients)
        return {"message": "Emails sent successfully!", "recipients": recipients}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
