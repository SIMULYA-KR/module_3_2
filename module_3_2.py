def send_email(message,recipient,sender = "university.help@gmail.com"):
    if ('@' and (".com" or ".ru" or ".net")) not in (recipient or sender):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    elif sender == recipient:
        print("Нельзя отправить  письмо самому себе!")
    elif sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    elif sender != "university.help.@gmail.com":
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")

send_email("Пожалуйста, исправьте задание","vlados.ru")
send_email("Пожалуйста, исправьте задание","vlados@.u")
send_email('Напоминаю самому себе о вебинаре',"university.help@gmail.com")
send_email("Вы видите это сообщение как лучший студент курса!","vlados@.com")
send_email('Это сообщение для проверки связи',"university.help@gmail.com","vlad.@mail.ru")