# Задайте переменные разных типов данных:
#   - Создайте переменную immutable_var и присвойте ей кортеж из нескольких элементов разных типов данных.
#   - Выполните операции вывода кортежа immutable_var на экран.
#
# 3. Изменение значений переменных:
#   - Попытайтесь изменить элементы кортежа immutable_var. Объясните, почему нельзя изменить значения элементов кортежа.
#
# 4. Создание изменяемых структур данных:
#   - Создайте переменную mutable_list и присвойте ей список из нескольких элементов.
#   - Измените элементы списка mutable_list.
#   - Выведите на экран измененный список mutable_list.

immutable_var = 10, 20, 30, True, 'Comfort'
print(immutable_var)
#immutable_var[0] = 100500  #TypeError: 'tuple' object does not support item assignment
#print(immutable_var)       #кортеж относится к неизменяемым типам данных, которые могут содержать в себе разные типы данных, в т.ч. списки

mutable_list = [ 'list', 10, 20, 30, True, 'Comfort']
print(mutable_list)
mutable_list[0] = 100
mutable_list[1] = 200
mutable_list[2] = 300
mutable_list[3] = 'Hello world'
mutable_list[4] = False
mutable_list[5] = 1011010101
print(mutable_list)