# Задача "Счётчик вызовов":
# Порой необходимо отслеживать, сколько раз вызывалась та или иная функция.
# К сожалению, в Python не предусмотрен подсчёт вызовов автоматически.
# Давайте реализуем данную фишку самостоятельно!
#
# Вам необходимо написать 3 функции:
# Функция count_calls подсчитывающая вызовы остальных функций.
# Функция string_info принимает аргумент - строку и возвращает кортеж из: длины этой строки, строку в верхнем регистре, строку в нижнем регистре.
# Функция is_contains принимает два аргумента: строку и список, и возвращает True, если строка находится в этом списке, False - если отсутствует.
# Регистром строки при проверке пренебречь: UrbaN ~ URBAN.

# Пункты задачи:
# Создать переменную calls = 0 вне функций.
# Создать функцию count_calls и изменять в ней значение переменной calls. Эта функция должна вызываться в остальных двух функциях.
# Создать функцию string_info с параметром string и реализовать логику работы по описанию.
# Создать функцию is_contains с двумя параметрами string и list_to_search, реализовать логику работы по описанию.
# Вызвать соответствующие функции string_info и is_contains произвольное кол-во раз с произвольными данными.
# Вывести значение переменной calls на экран(в консоль).

calls = 0
def count_calls ():  #подсчитывающая вызовы остальных функций.
    global calls
    calls += 1
    return calls
def string_info (data_in):  #принимает аргумент - строку и возвращает кортеж из: длины этой строки, строку в верхнем регистре, строку в нижнем регистре.
    data_string = str(data_in)
    data_len = len(data_string)
    data_out = (data_len, data_string.upper(), data_string.lower())
    count_calls()
    return data_out
def is_contains (data_in, data_list_in):  #ринимает два аргумента: строку и список, и возвращает True, если строка находится в этом списке, False - если отсутствует
    data_string = str(data_in.lower())
    data_list = list(data_list_in)
    data_out = False
    for i in range(len(data_list)):
        data_list[i] = data_list[i].lower()
        if data_string == data_list[i]:
            data_out = True
#   data_out = any(item in data_string for item in data_list)
    count_calls()
    return data_out

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(string_info('HellowWorld'))
print(string_info('GoodLuck'))

print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))    # No matches
print(is_contains('Kaban', ['Baklan', 'kaban', 'Baklan']))

print('Количество вызовов функции: ', calls)


