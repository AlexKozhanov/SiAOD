# -*- coding: cp1251 -*-
import math as math
class Triangle:
    "Класс создания переменной типа Треугольник и юазовые методы работы с треугольником"
    def __init__(self, a=3, b=4, c=5): # метод конструктор
        self.a, self.b, self.c = a, b, c
        # В Python метод __init__() имитирует конструктор класса
    def verisimilitude_check(self):
        if self.a > 0 and self.b > 0 and self.c > 0 \
            and self.a + self.b > self.c \
            and self.a + self.c > self.b \
            and self.b + self.c > self.a:
            return True
        else:
            return False
    def Perimeter (self):
        return self.a + self.b + self.c
    def Square(self):
        p = self.Perimeter() / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
    def __repr__(self): # метод вывода / возвращает представление, которое максимально похожа на Питоновский код
        if self.verisimilitude_check() == True:
            return "Треугольник(%s,%s,%s), Perimeter=%s, Square=%s" % (self.a, self.b, self.c, self.Perimeter() / 2, self.Square())
        else:
            return "Треугольник(%s,%s,%s) не существует" % (self.a, self.b, self.c, )

def main():
    triangle1 = Triangle()
    triangle2 = Triangle(6, 8, 10)
    triangle3 = Triangle(1, 3, 2)
    triangle4 = Triangle(-10, 400, 700)
    triangle5 = Triangle(15, 10, 8)
    list_triangle = [
        triangle1,
        triangle2,
        triangle3,
        triangle4,
        triangle5,
    ]
    for i in list_triangle:
        print(f"{i}")

if __name__ == "__main__":
    main()

# print(people.get("name"))
# print(people.get("имя", "Что это?"))
# print(people.setdefault(2)) # нетолько возвращает значение  ключа, но и создаёт новую пару
# people_copy = people.copy() # копия словаря
# print(people_copy)
# people.update({helena.key: helena}) # новые пары в словарь
# people.update({olga.key: helena}) # также если ключ есть, то перезапишет значение
# print(people.pop(olga.key)) # удаляет ключ и возвращает значение
# print(people.pop(helena.key, "No key!")) # если нет ключа, то возвращает переданное дефолтное значение
# print(people.popitem()) # удаляет и возвращает случайную пару ключ-значение
# print(people.keys()) возвращает список ключей словаря
# print(people.values()) возвращает список значений
# print(people.items()) возвращает кортежа с парами ключ-значение
# people.clear() # очищает словарь
# pprint(people)

# if __name__ == "__main__":

    # getattr(odj, name,[, default]) -
    # hasattr(odj, name) - проверяет на наличие атрибута name в obj
    # setattr(odj, name, value) - зкадает значение атрибута (если атрибут не существует, то он создается)
    # delattr(obj, name) - удаляет атрибут с именем name
    # class.__doc__ - содержит строку с описанием класса
    # *.__dict__  - содержит набор атрибутов экзэмпляра класса