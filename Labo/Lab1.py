import math as math
def calc_total_parallel_resist(r1: float, r2: float, r3: float)-> float:
    # 1) Сопротивления
    # Исходные данные, вводимые с клавиатуры: R1, R2, R3 значения (вещественные числа).
    # На экране выводится найденное значение выражения.
    R_rez=1 / (1 / r1 + 1 / r2 + 1 / r3)
    return R_rez

def calc_boat_path(v: float, v1: float, t1: float, t2: float)-> float:
    # 2) Вычисление пути  лодки
    # Исходные данные, вводимые с клавиатуры: значения V, V1, t1, t2 (вещественные числа).
    # На экране выводится найденное значение пути.
    S_rez = v * t1 + (v - v1) * t2
    return S_rez

def calc_function(x: float)-> float:
    # 3) Вычисление значения функции
    # Исходные данные, вводимые с клавиатуры: значение x (вещественное числа).
    # На экране выводится найденное значение функции.
    if x <= 3:
        x_rez = (-1 * x**2) + 3 * x + 9
    else:
        x_rez = math.sin(x) / (x - 9)
    return x_rez
def check_multiplicity_3(a: int)-> int:
    # 4) Проверка кратности 3
    a_rez = 0
    if a != 0 and a % 3 > 0:
        a_rez = 1 #'число не кратно 3'
    else:
        if a != 0 and a % 3 == 0:
            a_rez = 10 #'число кратно 3'
    return a_rez
def factorial(number: int):
    # 5) Факториал
    cos_sum = float(0)
    sin_sum = float(0)
    factorial = float(1)
    for i in range(1, number):
        cos_sum += math.cos(i)
        sin_sum += math.sin(i)
        factorial *= cos_sum / sin_sum
    return factorial
if __name__ == "__main__":
    command = input("Номер задания: ")
    match command.split():
        case ["1"]:
            R1 = input('Введите значения сопротивлений R1: ')
            R2 = input('R2: ')
            R3 = input('R3: ')
            R1 = float(R1)
            R2 = float(R2)
            R3 = float(R3)
            print(f'Значение общего сопротивления = \'{calc_total_parallel_resist(R1,R2,R3)}\' Ом')
        case ["2"]:
            V = input('Введите значения сопротивлений R1: ')
            V1 = input('Введите значения сопротивлений R1: ')
            T1 = input('Введите значения сопротивлений R1: ')
            T2 = input('Введите значения сопротивлений R1: ')
            V = float(V)
            V1 = float(V1)
            T1 = float(T1)
            T2 = float(T2)
            print(f'путь лодки = \'{calc_boat_path(V, V1, T1, T2)}\' Км')
        case ["3"]:
            X = input('Введите значение x: ')
            X = float(X)
            print(f'Найденное значение функции, F(\'{X}\') = \'{calc_function(X)}\'')
        case ["4"]:
            A = int(input('Введите значение x: '))
            B = int(input('Введите значение y: '))
            C = int(input('Введите значение z: '))
            if check_multiplicity_3(A) + check_multiplicity_3(B)  + check_multiplicity_3(C) == 21:
                print('Только два числа кратны 3')
            else:
                print('Условие, что только два числа кратны 3, не выполняется')
        case["5"]:
            Number = int(input('Введите число N: '))
            if Number <= 0:
                print('Неверные исходные данные!')
            else:
                print(f'Найденное значение выражения = \'{factorial(Number)}\'')