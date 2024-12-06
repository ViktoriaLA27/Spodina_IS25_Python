# Дано множество A из N точек (N > 2, точки заданы своими координатами x, у). Найти
# такую точку из данного множества, сумма расстояний от которой до остальных его
# точек минимальна, и саму эту сумму

import math

x_coords = []
y_coords = []

N = input("Введите количество точек: ")

while type(N) != int: # обработка исключений
    try:
        N = int(N)
        if N < 2:
            print("Неправильно ввели! Количество точек должно быть больше 2!")
            N = input("Введите число N:")
    except:
        print("Неправильно ввели! Введите целое число!")
        N = input("Введите число N:")

for i in range(N):
    x = input(f"Введите координату x для точки {i+1}: ")
    while type(x) != float:
        try:
            x = float(x)
        except:
            print("Неправильно ввели! Число должно быть вещественным!")
            x = input(f"Введите координату x для точки {i+1}: ")

    y = input(f"Введите координату y для точки {i+1}: ")
    while type(y) != float:
        try:
            y = float(y)
        except:
            print("Неправильно ввели! Число должно быть вещественным!")
            y = input(f"Введите координату x для точки {i+1}: ")

    x_coords.append(x)
    y_coords.append(y)

min_total_distance = float('inf')
min_point_index = -1

for i in range(len(x_coords)):
    total_distance = 0
    for j in range(len(x_coords)):
        if i != j:
            distance = math.sqrt((x_coords[i] - x_coords[j]) ** 2 + (y_coords[i] - y_coords[j]) ** 2)
            total_distance += distance
    if total_distance < min_total_distance:
        min_total_distance = total_distance
        min_point_index = i

print("\nТочка с минимальной суммой расстояний:")
print(f" x: {x_coords[min_point_index]}")
print(f" y: {y_coords[min_point_index]}")
print(f"Минимальная сумма расстояний: {min_total_distance}")
