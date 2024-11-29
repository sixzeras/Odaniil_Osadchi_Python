#Дано вещественное число X (|X|<1) и целое число N (>0). Найти значение выражения
#X - X3/3 + X5/5 - ... + (-1)NX2N +1/(2N +1). Полученное число является приближенным
#значением функции arctg в точке X.
try:
    x = float(input("Введите вещественное число x (|x| < 1): ")) #ввод чисел
    n = int(input("Введите целое число n (n > 0): "))

    while x > 0 and n <= 0: #проверка ввода чисел
        print('Неправильно ввели!')
        x = float(input("Введите вещественное число x (|x| < 1): "))
        n = int(input("Введите целое число n (n > 0): "))

    def arctg(x, n): #функция для вычисления данных
        result = 0
        for i in range(n):
            sign = (-1) ** i
            term = sign * x ** (2 * i + 1) / (2 * i + 1)
            result += term
        return result
    approx_value = arctg(x, n)
    print(f"Приближенное значение arctg({x}) для n={n}: {approx_value}")
except ValueError:
    print('Неправильно ввели!')


