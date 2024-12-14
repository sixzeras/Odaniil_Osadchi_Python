#Дан список размера N и целые числа K и L (1 < K ≤ L ≤ N). Найти среднее
#арифметическое всех элементов списка, кроме элементов с номерами от K до L
#включительно.
import random
#вводим размер списка
N = input("Введите размер списка N: ")

while type(N) != int: #проверка для исключения ошибок
    try:
        N = int(N)
    except:
        print('Число должно быть целым!')
        N = input("Введите размер списка N: ")

# Генерация случайных значений K и L
K = random.randint(2, N - 1)#K должно быть от 2 до N-1, чтобы 1 < K ≤ L ≤ N
L = random.randint(K, N)#L должно быть от K до N

#создаем список из N элементов
lst = list(range(1, N + 1))  # Например, список от 1 до N
print(f"Созданный список: {lst}")#выводим созданный список и числа для наглядности
print(f"Случайное значение K: {K}")
print(f"Случайное значение L: {L}")

def average_excluding_range(lst, K, L): #создаем функцию
    #исключаем элементы с индексами от K-1 до L
    excluded_elements = lst[:K - 1] + lst[L:]

    # Вычисляем сумму оставшихся элементов
    total_sum = sum(excluded_elements)

    # Вычисляем среднее арифметическое
    average = total_sum / len(excluded_elements)

    return average

# Вычисляем среднее арифметическое
result = average_excluding_range(lst, K, L)
print(f"Среднее арифметическое: {result}")


