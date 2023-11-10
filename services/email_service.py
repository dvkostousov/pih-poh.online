import os
import time

from itsdangerous import URLSafeTimedSerializer
from flask_mail import Message as MailMessage

from main import mail


def generate_confirmation_token(email):
    serializer = URLSafeTimedSerializer('ABC123')
    return serializer.dumps(email, salt='321CBA')


def confirm_token(token):
    serializer = URLSafeTimedSerializer('ABC123')
    try:
        email = serializer.loads(token, salt='321CBA', max_age=3600)
    except:
        return False
    return email


def send_email(to, subject, template):
    msg = MailMessage(subject, recipients=[to], html=template, sender='pihpoh188@gmail.com')
    print(4)
    mail.send(msg)
    print(5)
