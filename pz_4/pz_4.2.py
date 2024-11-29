#Дано число A (>1). Вывести наибольшее из целых чисел K, для которых сумма 1 +
#1/2 + ... + 1/K будет меньше A, и саму эту сумму.

A = input('Введите число A(>1): ') # ввод числа

while type(A) != float:  # исключение ошибок
    try:
        A = float(A)
    except ValueError:
        print("Неправильно ввели!")
        A = input('Введите число A(>1): ') # исключение ошибок

if A > 1: #проверка условий
    def find_max_k_and_sum(A): #функция
        K = 0
        sum_series = 0.0

        while sum_series < A: #пока сумма меньше а
            K += 1
            sum_series += 1 / K

        # Выводим предыдущее значение K и сумму
        print(f"Наибольшее K: {K - 1}")
        print(f"Сумма: {sum_series - 1 / K}")

    find_max_k_and_sum(A)
else:
    print("Неправильно ввели!")