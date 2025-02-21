from fastapi import FastAPI, HTTPException
from email_utils import send_greeting_email
from config import settings
import uvicorn

app = FastAPI()

@app.get("/")
def home():
    return {"message": "FastAPI Email Sender is Running!"}

@app.post("/send-email/")
def send_email(recipients: list[str]):
    try:
        send_greeting_email(recipients)
        return {"message": "Emails sent successfully!", "recipients": recipients}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app=app, host= "0.0.0.0", port= 8080)