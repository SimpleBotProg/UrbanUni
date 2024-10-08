# Задача "Рассылка писем":
# Часто при разработке и работе с рассылками писем(e-mail) они отправляются от одного и того же
# пользователя(администрации или службы поддержки). Тем не менее должна быть возможность сменить его в редких случаях.
# Попробуем реализовать функцию с подробной логикой.
#
# Создайте функцию send_email, которая принимает 2 обычных аргумента:
# сообщение и получатель и 1 обязательно именованный аргумент со значением по умолчанию - отправитель.
# Внутри функции реализовать следующую логику:
# Проверка на корректность e-mail отправителя и получателя.
# Проверка на отправку самому себе.
# Проверка на отправителя по умолчанию.
# Пункты задачи:
# Создайте функцию send_email, которая принимает 2 обычных аргумента:
# message(сообщение), recipient(получатель) и 1 обязательно именованный аргумент со значением по умолчанию sender = "university.help@gmail.com".
# Если строки recipient и sender не содержит "@" или не оканчивается на ".com"/".ru"/".net",
# то вывести на экран(в консоль) строку: "Невозможно отправить письмо с адреса <sender> на адрес <recipient>".
# Если же sender и recipient совпадают, то вывести "Нельзя отправить письмо самому себе!"
# Если же отправитель по умолчанию - university.help@gmail.com, то вывести сообщение: "Письмо успешно отправлено с адреса <sender> на адрес <recipient>."
# В противном случае вывести сообщение: "НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса <sender> на адрес <recipient>."
# Здесь <sender> и <recipient> - значения хранящиеся в этих переменных.
# За один вызов функции выводится только одно и перечисленных уведомлений! Проверки перечислены по мере выполнения.

def send_email(message, recipient, sender='university.help@gmail.com'):
    # переводим все в нижний регистр
    recipient = recipient.lower()
    sender = sender.lower()
    check_sym = '@'
    check_list = ['.com', '.ru', '.net']
    bFlag_11 = False  # обнуляем первоначальные значения
    bFlag_12 = False  # обнуляем первоначальные значения
    bFlag_21 = False  # обнуляем первоначальные значения
    bFlag_22 = False  # обнуляем первоначальные значения

    # проверяем получателя на наличие спец символов
    bFlag_11 = any(item in check_sym for item in recipient)

    # проверяем получателя на наличие спец символов
    for i in range(len(check_list)):
        recip_cor = recipient.find(check_list[i])
        if recip_cor != -1:  # если хотя бы одно выражение найдено - взводим флаг
            bFlag_12 = True
            break

    # проверяем отправителя на наличие спец символов
    bFlag_21 = any(item in check_sym for item in sender)

    #  проверяем отправителя на наличие спец символов
    for i in range(len(check_list)):
        sender_cor = sender.find(check_list[i])
        if sender_cor != -1:  # если хотя бы одно выражение найдено - взводим флаг
            bFlag_22 = True
            break

    # если 4 условия корректности заполнения email выполняются - отправить email возможно
    if bFlag_11 == True and bFlag_12 == True and bFlag_21 == True and bFlag_22 == True:
        # если отправитель и получатель - совпадают, то нельзя отправить самому себе
        if sender != recipient:
            if sender == 'university.help@gmail.com':
                print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
            elif sender != 'university.help@gmail.com':
                print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')
        else:
            print('Нельзя отправить письмо самому себе!')
    else:
     print(f'Неозможно отправить письмо с адреса {sender} на адрес {recipient}')

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
