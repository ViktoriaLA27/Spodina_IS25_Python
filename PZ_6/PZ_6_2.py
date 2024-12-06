# Дан целочисленный список A размера N (< 15). Переписать в новый целочисленный
# список B все элементы с нечетными порядковыми номерами (1,3,...) и вывести
# размер полученного списка B и его содержимое. Условный оператор не
# использовать.

N = input("Введите размер списка A: ")
while type(N) != int: # обработка исключений
    try:
        N = int(N)
        if N < 0:
            print("Неправильно ввели! Число N должно быть положительным!")
            N = input("Введите размер списка A: ")
        elif N >= 15:
            print("Неправильно ввели! Число N должно быть строго меньше 15!")
            N = input("Введите размер списка A: ")
    except:
        print("Неправильно ввели! Введите целое число!")
        N = input("Введите размер списка A: ")

A = []

for i in range(N):
    while True:
        try:
            num = int(input(f"Введите элемент {i + 1}: "))
            A.append(num)
            break
        except ValueError:
            print("Неправильно ввели!")

B = A[1::2]

print("Размер списка B:", len(B))
print("Содержимое списка B:", B)
