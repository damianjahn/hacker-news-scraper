from abc import ABC, abstractmethod
from Scraper.email_service import send_email

class EmailSender(ABC):
    @abstractmethod
    def send(self, subject: str, body: str, attachment_path: str = None):
        pass

class SmtpEmailSender(EmailSender):
    def __init__(self, sender_email, receiver_email, smtp_server, smtp_port, smtp_password):
        self.sender_email = sender_email
        self.receiver_email = receiver_email
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.smtp_password = smtp_password

    def send(self, subject, body, attachment_path=None):
        send_email(
            subject=subject,
            body=body,
            sender_email=self.sender_email,
            receiver_email=self.receiver_email,
            smtp_server=self.smtp_server,
            smtp_port=self.smtp_port,
            smtp_password=self.smtp_password,
            attachment_path=attachment_path
        )