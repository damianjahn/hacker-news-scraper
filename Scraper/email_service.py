import smtplib
from email.mime.text import MIMEText

def send_email(subject, body, sender_email, receiver_email, smtp_server, smtp_port, smtp_password):
    msg = MIMEText(body, "plain", "utf-8")
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = receiver_email

    with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
        server.login(sender_email, smtp_password)
        server.send_message(msg)

    print("✅ Email sent successfully.")