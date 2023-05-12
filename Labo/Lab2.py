import math as math
import numpy as np
def calc_decimal1(x: float, y: float)-> float:
    # 1) Дробь1
    # Исходные данные, вводимые с клавиатуры: значения x, y (вещественные числа).
    # На экране выводится найденное значение выражения.
    R_rez = (1 + math.sin(math.sqrt(x+1))) / (math.cos(12*y - 4))
    return R_rez

def calc_decimal2(x: float, y: float)-> float:
    # 2) Дробь2
    # Исходные данные, вводимые с клавиатуры: значения x, y (вещественные числа).
    # На экране выводится найденное значение выражения.
    R_rez = (1 + math.pow(math.sin(x + y), 2)) \
            / (2 + abs(x - ((2 * x) / (1 + math.pow(x, 2) * math.pow(y, 2))))) \
            + x
    return R_rez

def calc_function1():
    # 3) Оператор match (Аналог switch в Python)
    # Исходные данные, вводимые с клавиатуры: действительное число x, номер действия.
    # На экране выводится:
    # - значение выражения (если данные введены корректно)
    # - сообщение, что действие выполнить невозможно
    # - сообщение, что введен неверный номер действия
    z_x = float(input('Введите X: '))
    z_command = input("Номер действия, где "
                      "1-квадрат 2-корень 3-корень3степени 4-модуль 5-натурлог")
    match z_command.split():
        case ["1"]:
            a = math.pow(z_x, 2)
            print(f'Квадрат = \'{a}\'')
        case ["2"]:
            if z_x > 0:
                b = math.sqrt(z_x)
                print(f'Корень из X = \'{b}\'')
            else:
                print('Действие выполнить невозможно')
        case ["3"]:
            c = np.cbrt(z_x)
            print(f'Кубический корень из X = \'{c}\'')
        case ["4"]:
            print(f'Кубический корень из X = \'{abs(z_x)}\'')
        case ["5"]:
            print(f'Натуральный логарифм X = \'{math.log(z_x)}\'')
        case _:
            print("Введен неверный номер действия")
def calc_decimal3(c):
    # 4) Дробь3
    rez = 1
    z_list = [2, 4, 8, 16, 32, 64]
    for i in z_list:
        if c == i:
            rez += 1
    if rez == 1:
        for i in z_list:
            rez *= (c - i + 1) / (c - i)
        print(f'Результат = \'{rez}\'')
    else:
        print('Деление на 0')

if __name__ == "__main__":
    command = input("Номер задания: ")
    match command.split():
        case ["1"]:
            X = float(input('Введите X: '))
            Y = float(input('Введите Y: '))
            print(f'Результат = \'{calc_decimal1(X, Y)}\'')
        case ["2"]:
            X = float(input('Введите X: '))
            Y = float(input('Введите Y: '))
            print(f'Результат = \'{calc_decimal2(X, Y)}\'')
        case ["3"]:
            calc_function1()
        case ["4"]:
            X = int(input('Введите X: '))
            calc_decimal3(X)
        case _:
            print('Введи другое')