import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from config.settings import settings


def send(receiver, subject, message):
    msg = MIMEMultipart()
    msg['From'] = settings.SMTP_USER
    msg['To'] = receiver
    msg['Subject'] = subject

    # Ajouter le corps du message
    msg.attach(MIMEText(message, 'plain'))

    try:
        # Connexion au serveur SMTP
        serveur_smtp = smtplib.SMTP(settings.SMTP_HOST, settings.SMTP_PORT)
        serveur_smtp.starttls()  # Sécurise la connexion

        # Connexion avec les informations d'authentification
        serveur_smtp.login(settings.SMTP_USER, settings.SMTP_PASSWORD)

        # Envoi de l'e-mail
        serveur_smtp.sendmail(settings.SMTP_USER, receiver, msg.as_string())

        # logging.info(f'Email envoyé à {destinataire}')
    except Exception as e:
        pass
        # logging.info(f'Error with the email : {e}')
        # time.sleep(5*60)
    finally:
        # Fermer la connexion au serveur SMTP
        serveur_smtp.quit()