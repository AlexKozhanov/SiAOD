# -*- coding: cp1251 -*-
import math as math
class Triangle:
    "����� �������� ���������� ���� ����������� � ������� ������ ������ � �������������"
    def __init__(self, a=3, b=4, c=5): # ����� �����������
        self.a, self.b, self.c = a, b, c
        # � Python ����� __init__() ��������� ����������� ������
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
    def __repr__(self): # ����� ������ / ���������� �������������, ������� ����������� ������ �� ����������� ���
        if self.verisimilitude_check() == True:
            return "�����������(%s,%s,%s), Perimeter=%s, Square=%s" % (self.a, self.b, self.c, self.Perimeter() / 2, self.Square())
        else:
            return "�����������(%s,%s,%s) �� ����������" % (self.a, self.b, self.c, )

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
# print(people.get("���", "��� ���?"))
# print(people.setdefault(2)) # �������� ���������� ��������  �����, �� � ������ ����� ����
# people_copy = people.copy() # ����� �������
# print(people_copy)
# people.update({helena.key: helena}) # ����� ���� � �������
# people.update({olga.key: helena}) # ����� ���� ���� ����, �� ����������� ��������
# print(people.pop(olga.key)) # ������� ���� � ���������� ��������
# print(people.pop(helena.key, "No key!")) # ���� ��� �����, �� ���������� ���������� ��������� ��������
# print(people.popitem()) # ������� � ���������� ��������� ���� ����-��������
# print(people.keys()) ���������� ������ ������ �������
# print(people.values()) ���������� ������ ��������
# print(people.items()) ���������� ������� � ������ ����-��������
# people.clear() # ������� �������
# pprint(people)

# if __name__ == "__main__":

    # getattr(odj, name,[, default]) -
    # hasattr(odj, name) - ��������� �� ������� �������� name � obj
    # setattr(odj, name, value) - ������� �������� �������� (���� ������� �� ����������, �� �� ���������)
    # delattr(obj, name) - ������� ������� � ������ name
    # class.__doc__ - �������� ������ � ��������� ������
    # *.__dict__  - �������� ����� ��������� ���������� ������