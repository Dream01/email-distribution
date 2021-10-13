from configs import password
import smtplib, ssl

server = None
sender = 'sender@gmail.com'  # імейл відправника
context = ssl.create_default_context()  # містить переважно значення за замовчуванням для структур SSL, які пізніше створюються для з'єднань.
users = ['user@gmail.com']  # список отримувачів
subject = 'Python mini course'  # Заголовок листа
m = 'Hi there,\n How are you?'  # Повідомлення
message = f'Subject: {subject}\n\n{m}'  # Сукупність заголовка та повідомлення для відправки

try:
    server = smtplib.SMTP(host='smtp.gmail.com', port=587)  # створення незахищеного з'єднання з сервером
    server.ehlo()  # Сенс команди полягає в представленні клієнта серверу SMTP.
    server.starttls(context=context)  # створення безпечного з'єднання з сервером
    server.ehlo()  # Сенс команди полягає в представленні клієнта серверу SMTP.
    server.login(user=sender, password=password)  # логування користувача до сервера
    for user in users:  # прохід по кожному користувачі зі списку для відправки
        server.sendmail(from_addr=sender, to_addrs=user, msg=message)  # відправка кожному користувачеві повідомлення
except Exception as e:  # оброляє помилки якщо є
    print(e)  # вивід помилки якщо є
finally:  #
    server.quit()  # вкінці закриває з'єднання з сервером

# with smtplib.SMTP(host='smtp.gmail.com', port=587) as server:
#     server.ehlo()
#     server.starttls(context=context)
#     server.ehlo()
#     server.login(user=sender, password=password)
#     for user in users:
#         server.sendmail(from_addr=sender, to_addrs=user, msg=message)
