from configs import password

import smtplib, ssl
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

sender = 'sender@gmail.com'
users = ['user@gmail.com']
all_users = ", ".join(users)

message = MIMEMultipart()
message['Subject'] = 'Lecture 2 about Emails'
message['From'] = sender
message['To'] = all_users

lecture_text = MIMEText('Hello, there! \nPlease take a look at this lecture!', 'plain')

message.attach(lecture_text)

filename = 'email_lecture_2.pdf'

with open(filename, 'rb') as attachment:
    part = MIMEBase('application/pdf', "octet-stream")
    part.set_payload(attachment.read())

encoders.encode_base64(part)
part.add_header("Content-Disposition", f'attachment; filename={filename}')
message.attach(part)
text = message.as_string()

context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
    server.login(user=sender, password=password)
    server.ehlo()
    server.sendmail(sender, users, text)
