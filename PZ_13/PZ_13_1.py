# В двумерном списке найти среднее арифметическое положительных элементов,
# кратных 3.
import random

a = int(input('Введите количество строк: '))
b = int(input('Введите количество элементов в строке: '))

matrix = [[random.randint(-100,100) for i in range(a)] for i in range(b)]

print('Сгенерированная матрица: ')
for row in matrix:
    print(row)

new_list = [number for row in matrix for number in row if number > 0 and number % 3 == 0]
print("Список положительных элементов, кратных 3:", new_list)
if not new_list:
    print("Числа не найдены")
else:
    sred = sum(new_list) / len(new_list)
    print("Среднее арифметическое положительных элементов, кратных 3:", sred)
