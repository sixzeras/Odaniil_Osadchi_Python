#Найти сумму чисел ряда 1,2,3,...,60 с использованием функции нахождения суммы.
#Использовать локальные переменные
def sum_of_series(start, end):
    total_sum = 0 #Локальная переменная для хранения суммы
    for number in range(start, end + 1): #Цикл для суммирования чисел от start до end
        total_sum += number

    return total_sum

result = sum_of_series(1, 60)

print("Сумма чисел от 1 до 60 равна:", result) #Вывод результата
