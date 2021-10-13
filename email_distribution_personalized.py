import csv
import smtplib, ssl
from configs import password
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

html_message = """
<head>
    <style>
        #customstyle {
        border: 2px solid red;
        border-radius: 25px;
        padding: 50px;
        }
    </style>
</head>
<body>
<div id="customstyle">
    <center>
        <div style='font-family: Courier; font-weight:normal; padding:20px; font-size: 20px'>
            <a>Hi %s, tomorrow we will have a planned an electricity outage, please take your devices off.<br> Thanks is advance!</a>        </div>
    </center>
</div>
</body>
"""
sender = 'sender@gmail.com'
message = MIMEMultipart()
message['Subject'] = 'Service outage'
message['From'] = sender

context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
    server.login(user=sender, password=password)
    server.ehlo()
    with open('users.csv') as file:
        reader = csv.reader(file)
        next(reader)
        for name, email, m in reader:
            message['To'] = email
            part2 = MIMEText(html_message % name, 'html')
            message.attach(part2)
            server.sendmail(sender, email, message.as_string())
