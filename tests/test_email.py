from unittest.mock import patch
from src.utils import email


def test_send_email():
    with patch("smtplib.SMTP") as mock_smtp:
        instance = mock_smtp.return_value

        assert email.send("test@example.com", "subject", "body")

        instance.sendmail.assert_called_once()
