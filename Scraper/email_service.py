import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import os

def send_email(subject, body, sender_email, receiver_email, smtp_server, smtp_port, smtp_password, attachment_path=None):
    msg = MIMEMultipart()
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = receiver_email

    # Add the email body as plain text
    msg.attach(MIMEText(body, "plain", "utf-8"))

    # Add CSV attachment if provided
    if attachment_path and os.path.exists(attachment_path):
        with open(attachment_path, "rb") as f:
            part = MIMEApplication(f.read(), _subtype="csv")
            part.add_header("Content-Disposition", "attachment", filename=os.path.basename(attachment_path))
            msg.attach(part)

    # Send email
    with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
        server.login(sender_email, smtp_password)
        server.send_message(msg)

    print("✅ Email sent successfully.")