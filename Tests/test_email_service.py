import os
import tempfile
from unittest.mock import patch, Mock
from Scraper.email_service import send_email

@patch("smtplib.SMTP_SSL")
def test_send_email_without_attachment(mock_smtp):
    mock_server = Mock()
    mock_smtp.return_value.__enter__.return_value = mock_server

    send_email(
        subject="Test Email",
        body="This is a test.",
        sender_email="test@example.com",
        receiver_email="receiver@example.com",
        smtp_server="smtp.example.com",
        smtp_port=465,
        smtp_password="fakepassword"
    )

    mock_server.login.assert_called_once_with("test@example.com", "fakepassword")
    mock_server.send_message.assert_called_once()

@patch("smtplib.SMTP_SSL")
def test_send_email_with_attachment(mock_smtp):
    mock_server = Mock()
    mock_smtp.return_value.__enter__.return_value = mock_server

    with tempfile.NamedTemporaryFile(delete=False) as tmpfile:
        tmpfile.write(b"test content")
        tmpfile_path = tmpfile.name

    try:
        send_email(
            subject="Test Email with Attachment",
            body="This is a test.",
            sender_email="test@example.com",
            receiver_email="receiver@example.com",
            smtp_server="smtp.example.com",
            smtp_port=465,
            smtp_password="fakepassword",
            attachment_path=tmpfile_path
        )

        mock_server.login.assert_called_once_with("test@example.com", "fakepassword")
        mock_server.send_message.assert_called_once()
    finally:
        os.remove(tmpfile_path)