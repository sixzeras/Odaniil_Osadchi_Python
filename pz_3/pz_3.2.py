#Даны два числа. Вывести большее из них.
x = input('Введите первое число: ')
y = input('Введите второе число: ')

while type(x) != int:  #исключение ошибок
    try:
        x = int(x)
    except ValueError:
        print("Неправильно ввели!")
        x = input("Введите первое число: ")

while type(y) != int:  #исключение ошибок
    try:
        y = int(y)
    except ValueError:
        print("Неправильно ввели!")
        y = input("Введите Второе число: ")

if x > y: #выясняем какое из данных чисел больше
    print(x)
else:
    print(y)

