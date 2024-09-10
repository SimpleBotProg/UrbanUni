# Задача "История строительства":
# В классе House создайте атрибут houses_history = [], который будет хранить названия созданных объектов.
#
# Правильней вписывать здание в историю сразу при создании объекта,
# тем более можно удобно обращаться к атрибутам класса используя ссылку на сам класс - cls.
# Дополните метод __new__ так, чтобы:
# Название объекта добавлялось в список cls.houses_history.
# Название строения можно взять из args по индексу.
#
# Также переопределите метод __del__(self) в котором будет выводиться строка:
# "<название> снесён, но он останется в истории"
#
# Создайте несколько объектов класса House и проверьте работу методов __del__ и __new__,
# а также значение атрибута houses_history.


class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
#        print ('Im in new')
            house_name = args[0]
            cls.houses_history.append(house_name)
            return super().__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.number_of_floors:
            print('Такого этажа не существует')
        else:
            for i in range(new_floor):
                print(i + 1)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название {self.name}, количество этажей {self.number_of_floors}'

    def __eq__(self, other):  # hравно
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors == other
    #        return self.number_of_floors == other.number_of_floors

    def __gt__(self, other):  # больше
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors > other
    #        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):  # больше или равно
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors >= other
    #        return self.number_of_floors >= other.number_of_floors

    def __lt__(self, other):  # меньше
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors < other
    #       return self.number_of_floors < other.number_of_floors

    def __le__(self, other):  # меньше или равно
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors <= other
    #        return self.number_of_floors <= other.number_of_floors

    def __ne__(self, other):  # не равно
        if isinstance(other, House):
            self.number_of_floors != other.number_of_floors
        elif isinstance(other, int):
            self.number_of_floors != other
        return self.number_of_floors != other
    #   return self.number_of_floors != other.number_of_floors

    def __add__(self, other):  # add
        #   self.number_of_floors + other
        #   if isinstance(other, int):
        if isinstance(other, House):
            self.number_of_floors += other.number_of_floors
        elif isinstance(other, int):
            self.number_of_floors += other
        return self

    def __iadd__(self, other):
        #    self.number_of_floors += other
        # if isinstance(other, House):
        #     self.number_of_floors += other.number_of_floors
        # elif isinstance(other, int):
        #     self.number_of_floors += other
        return self.__add__(other)

    def __radd__(self, other):
        #    other + self.number_of_floors
        # if isinstance(other, House):
        #     self.number_of_floors += other.number_of_floors
        # elif isinstance(other, int):
        #     self.number_of_floors += other
        return self.__add__(other)

    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)



# h1 = House('ЖК Эльбрус', 10)
# h2 = House('ЖК Акация', 20)
#
# print(h1)
# print(h2)
#
# print(h1 == h2)  # __eq__
#
# h1 = h1 + 10  # __add__
# print(h1)
# print(h1 == h2)
#
# h1 += 10  # __iadd__
# print(h1)
#
# h2 = 10 + h2  # __radd__
# print(h2)
#
# print(h1 > h2)  # __gt__
# print(h1 >= h2)  # __ge__
# print(h1 < h2)  # __lt__
# print(h1 <= h2)  # __le__
# print(h1 != h2)  # __ne__
