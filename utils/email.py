import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from config.settings import settings
from utils.logger import logging


def send(receiver: str, subject: str, message: str):
    """
    Returns True or False according to the sending of the email.

    Args:
        receiver (str): Receiver of the mail
        subject (str): Subject of the mail
        message (str): The content of the mail

    Returns:
        Bool value
    """

    msg = MIMEMultipart()
    msg["From"] = settings.SMTP_USER
    msg["To"] = receiver
    msg["Subject"] = subject

    result = False

    msg.attach(MIMEText(message, "plain"))

    try:
        serveur_smtp = smtplib.SMTP(settings.SMTP_HOST, settings.SMTP_PORT)
        serveur_smtp.starttls()

        serveur_smtp.login(settings.SMTP_USER, settings.SMTP_PASSWORD)

        serveur_smtp.sendmail(settings.SMTP_USER, receiver, msg.as_string())

        logging.info(f"Email envoyé à {receiver}")
        result = True
    except Exception as e:
        logging.warning(f"Error with the email : {e}")
        result = False
    finally:
        serveur_smtp.quit()
        return result
