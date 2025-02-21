import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from app.config import settings

def send_greeting_email(recipients: list[str]):
    if not settings.SMTP_USERNAME or not settings.SMTP_PASSWORD:
        raise ValueError("SMTP credentials are missing. Check environment variables.")

    subject = "Greetings from FastAPI!"
    body = "Hello! This is a test email sent using FastAPI."

    msg = MIMEMultipart()
    msg["From"] = settings.SENDER_EMAIL
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    try:
        with smtplib.SMTP(settings.SMTP_SERVER, settings.SMTP_PORT) as server:
            server.starttls()
            server.login(settings.SMTP_USERNAME, settings.SMTP_PASSWORD)

            # Send email to multiple recipients correctly
            server.sendmail(settings.SENDER_EMAIL, recipients, msg.as_string())

        print("Emails sent successfully!")
    except Exception as e:
        print(f"Error sending emails: {e}")
        raise
