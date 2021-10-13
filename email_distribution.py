from configs import password
import smtplib
import ssl

sender = 'sender@gmail.com'  # імейл відправника
context = ssl.create_default_context()  # містить переважно значення за замовчуванням для структур SSL, які пізніше створюються для з'єднань.
users = ['user@gmail.com']  # список отримувачів
subject = 'Python mini course'  # Заголовок листа
m = 'Hi there,\n How are you?'  # Повідомлення
message = f'Subject: {subject}\n\n{m}'  # Сукупність заголовка та повідомлення для відправки

with smtplib.SMTP_SSL(host='smtp.gmail.com', port=465,
                      context=context) as server:  # створення захищеного з'єднання з сервером
    server.login(user=sender, password=password)  # логування користувача до сервера
    server.ehlo()  # Сенс команди полягає в представленні клієнта серверу SMTP.
    for user in users:  # прохід по кожному користувачі зі списку для відправки
        server.sendmail(sender, user, msg=message)  # відправка кожному користувачеві повідомлення

# try:
#     server = smtplib.SMTP_SSL(host='smtp.gmail.com', port=465, context=context)
#     server.login(user=sender, password=password)
#     server.ehlo()
#     for user in users:
#         server.sendmail(sender, user, msg=message)
# except Exception as e:
#     print(e)
# finally:
#     server.quit()
