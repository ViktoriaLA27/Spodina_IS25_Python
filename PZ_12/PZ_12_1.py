# В последовательности их N чисел (N –четное) в первой ее половине найти
# произведение элементов меньших 0.
import random

N = 6
a = [random.randint(-20, 20) for i in range(N)]

first = a[:N // 2]

n_el = list(filter(lambda x: x < 0, first))

if not n_el:
    b = 0
else:
    b = 1
    for num in n_el:
        b *= num

print(f"Исходная последовательность:", a)
print("Произведение отрицательных элементов в первой половине:", b)
