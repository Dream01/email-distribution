import csv
import smtplib, ssl
import re
from email_configs import provider

from configs import password
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from templates.basic_templates import *


def get_email_provider(email):
    regexp = '(@\w+.\w+)'
    mail_service = re.findall(regexp, email)
    print(mail_service)
    mail_service = mail_service[0]
    return mail_service


mail_type = input('Enter your email type: ')
while mail_type not in templates_lst:
    mail_type = input(f'Enter your email type from the list {templates_lst}: ')
subject = input('Enter your subject: ')
body = input('Enter your email text: ')

sender = ''
message = MIMEMultipart()
message['Subject'] = subject
message['From'] = sender

email_provider = get_email_provider(sender)

context = ssl.create_default_context()
with smtplib.SMTP_SSL(provider[email_provider]['host'], provider[email_provider]['port'], context=context) as server:
    server.login(user=sender, password=password)
    server.ehlo()
    with open('users.csv') as file:
        reader = csv.reader(file)
        next(reader)
        for name, email in reader:
            message['To'] = email
            email_type = eval(mail_type)
            text = email_type.replace('{name}', name).replace('{data}', body)
            email_text = MIMEText(text, 'html')
            message.attach(email_text)
            server.sendmail(sender, email, message.as_string())
