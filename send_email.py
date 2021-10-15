import csv
import smtplib, ssl
import argparse

from configs import password
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from templates.basic_templates import *

parser = argparse.ArgumentParser(description='Email distribution helper')
parser.add_argument('--email_type', help='Choose your email type', dest='email_type', required=True)
parser.add_argument('--subject', help='Email subject', dest='subject', required=True, nargs='+')
parser.add_argument('--body', help='Email text body', dest='body', required=True, nargs='+')
args = parser.parse_args()

sender = ''
message = MIMEMultipart()
message['Subject'] = ' '.join(args.subject)
message['From'] = sender

context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
    server.login(user=sender, password=password)
    server.ehlo()
    with open('users.csv') as file:
        reader = csv.reader(file)
        next(reader)
        for name, email in reader:
            message['To'] = email
            email_type = eval(args.email_type)
            text = email_type.replace('{name}', name).replace('{data}', ' '.join(args.body))
            email_text = MIMEText(text, 'html')
            message.attach(email_text)
            server.sendmail(sender, email, message.as_string())

