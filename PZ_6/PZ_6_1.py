# Дан список ненулевых целых чисел размера N. Проверить, чередуются ли в нем
# положительные и отрицательные числа. Если чередуются, то вывести 0, если нет, то
# вывести порядковый номер первого элемента, нарушающего закономерность.

N = input("Введите число N: ")

while type(N) != int: # обработка исключений
    try:
        N = int(N)
        if N < 0:
            print("Неправильно ввели! Число N должно быть положительным!")
            N = input("Введите число N:")
    except:
        print("Неправильно ввели! Введите целое число!")
        N = input("Введите число N:")

numbers = []
for i in range(N):
    num = input(f"Введите число {i+1}: ")
    while type(num) != int: # обработка исключений
        try:
            num = int(num)
            if num == 0:
                print("Неправильно ввели! Введите целое число!")
                num = input(f"Введите число {i + 1}: ")
        except:
            print("Неправильно ввели! Введите целое число!")
            num = input(f"Введите число {i+1}: ")
    numbers.append(num)
    continue


violation_index = 0
for i in range(1, N):
    if (numbers[i] < 0 and numbers[i-1] < 0) or ( numbers[i] > 0 and numbers[i-1] > 0):
        violation_index = i + 1
        break

print(violation_index)