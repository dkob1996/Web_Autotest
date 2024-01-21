import smtplib
from email.mime.text import MIMEText
import yaml
#from paths.static_paths import *

#with open(yaml_mailer_data()) as f:
with open('/Users/dmitrii_kobozev/Desktop/Web_Autotests/Sem3/Mailer/mail_data.yaml') as f:
    mail_data = yaml.safe_load(f)

subject = mail_data['gmail_subject']
body = mail_data['gmail_body']
sender = mail_data['gmail_sender']
recipients = mail_data['gmail_recipients']
password = mail_data['gmail_password']


def send_email(subject, body, sender, recipients, password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
       smtp_server.login(sender, password)
       smtp_server.sendmail(sender, recipients, msg.as_string())
    print("Message sent!")


send_email(subject, body, sender, recipients, password)