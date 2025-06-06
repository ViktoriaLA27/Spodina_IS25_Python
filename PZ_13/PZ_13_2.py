# В двумерном списке элементы строки N (N задать с клавиатуры) увеличить на 3
import random

a = int(input('Введите количество строк: '))
b = int(input('Введите количество элементов в строке: '))

matrix = [[random.randint(-100,100) for i in range(a)] for i in range(b)]

print('Сгенерированная матрица: ')
for row in matrix:
    print(row)

N = int(input('Введите номер строки N: '))
if 1 <= N <= a:
    matrix[N - 1] = list(map(lambda x: x + 3, matrix[N - 1]))
    print('Обновленная матрица:')
    for row in matrix:
        print(row)
else:
    print('Неправильно введен номер строки')

