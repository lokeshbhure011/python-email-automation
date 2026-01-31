import smtplib
import os
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()

def send_email(subject, body, attachment=None):
    sender = os.getenv("SENDER_EMAIL")
    password = os.getenv("APP_PASSWORD")
    receiver = os.getenv("RECEIVER_EMAIL")

    msg = EmailMessage()
    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"] = subject
    msg.set_content(body)

    if attachment:
        with open(attachment, "rb") as f:
            msg.add_attachment(
                f.read(),
                maintype="application",
                subtype="octet-stream",
                filename=os.path.basename(attachment)
            )

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender, password)
        server.send_message(msg)

    print("Email sent successfully")


# ---------- Run ----------
sub = input("Subject: ")
body = input("Message: ")
attach = input("Enter attachment path (or press Enter to skip): ")

try:
    send_email(sub, body, attach if attach.strip() else None)
except Exception as e:
    print("Failed to send email:", e)
