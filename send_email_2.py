import csv
import smtplib, ssl

from configs import password
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from templates.basic_templates import *

mail_type = input('Enter your email type: ')
while mail_type not in templates_lst:
    mail_type = input(f'Enter your email type from the list {templates_lst}: ')
subject = input('Enter your subject: ')
body = input('Enter your email text: ')

sender = ''
message = MIMEMultipart()
message['Subject'] = subject
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
            email_type = eval(mail_type)
            text = email_type.replace('{name}', name).replace('{data}', body)
            email_text = MIMEText(text, 'html')
            message.attach(email_text)
            server.sendmail(sender, email, message.as_string())
