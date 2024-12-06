#Описать функцию Mean(X, Y, AMean, GMean), вычисляющую среднее
#арифметическое AMean = (X+Y)/2 и среднее геометрическое GMean = y/X Y двух
#положительных чисел X и Y (X и Y — входные, AMean и GMean — выходные
#параметры вещественного типа). С помощью этой функции найти среднее
#арифметическое и среднее геометрическое для пар (A, B), (A, C), (A, D), если даны
#A, B, C, D.
import math

# Ввод значений A, B, C, D
A = input("Введите значение A: ")
B = input("Введите значение B: ")
C = input("Введите значение C: ")
D = input("Введите значение D: ")

while type(A) != float:  # исключение ошибок
    try:
        A = float(A)
    except ValueError:
        print("Неправильно ввели!")
        A = input("Введите значение A: ")

while type(B) != float:  # исключение ошибок
    try:
        B = float(B)
    except ValueError:
        print("Неправильно ввели!")
        B = input("Введите значение B: ")

while type(C) != float:  # исключение ошибок
    try:
        C = float(C)
    except ValueError:
        print("Неправильно ввели!")
        C = input("Введите значение C: ")

while type(D) != float:  # исключение ошибок
    try:
        D = float(D)
    except ValueError:
        print("Неправильно ввели!")
        D = input("Введите значение D: ")

if A and B and C and D > 0:
    def Mean(X, Y, AMean, GMean):
        AMean[0] = (X + Y) / 2 #Вычисление среднего арифметического
        GMean[0] = math.sqrt(X * Y) # Вычисление среднего геометрического

    #Массивы для хранения результатов
    AMean_AB = [0]
    GMean_AB = [0]

    AMean_AC = [0]
    GMean_AC = [0]

    AMean_AD = [0]
    GMean_AD = [0]

    # Вычисление средних для пар (A, B), (A, C), (A, D)
    Mean(A, B, AMean_AB, GMean_AB)
    Mean(A, C, AMean_AC, GMean_AC)
    Mean(A, D, AMean_AD, GMean_AD)

    # Вывод результатов
    print(f"Среднее арифметическое и геометрическое для пары (A, B): {AMean_AB[0]}, {GMean_AB[0]}")
    print(f"Среднее арифметическое и геометрическое для пары (A, C): {AMean_AC[0]}, {GMean_AC[0]}")
    print(f"Среднее арифметическое и геометрическое для пары (A, D): {AMean_AD[0]}, {GMean_AD[0]}")
else:
    print('Числа должны быть целыми!')
