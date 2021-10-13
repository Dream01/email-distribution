from configs import password

import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender = 'sender@gmail.com'
users = ['user@gmail.com']
all_users = ", ".join(users)

message = MIMEMultipart('alternative')
message['Subject'] = 'Multipart message'
message['From'] = sender
message['To'] = all_users

text = """
Hi there, 
This is the first try of sending an email.
Please reach the www.google.com for more details.
"""

html_text = """
<html>
<body>
<p>Hi there,<br>
    Please reach the <a href="https://google.com">Google</a>
    for more details.
</p>
</body>
</html>
"""

part1 = MIMEText(text, "plain")
part2 = MIMEText(html_text, 'html')

message.attach(part1)
message.attach(part2)

context = ssl.create_default_context()

with smtplib.SMTP_SSL(host='smtp.gmail.com', port=465,
                      context=context) as server:  # створення захищеного з'єднання з сервером
    server.login(user=sender, password=password)  # логування користувача до сервера
    server.ehlo()
    server.sendmail(sender, users, message.as_string())
