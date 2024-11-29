# Описать функцию InvertDigits(K), меняющую порядок следования цифр целого
# положительного числа K на обратный (K — параметр целого типа, являющийся
# одновременно входным и выходным). С помощью этой функции поменять порядок
# следования цифр на обратный для каждого из пяти данных целых чисел.

def invert_digits(k):
    if k < 0:
        raise ValueError("Неправильно ввели! Число должно быть неотрицательным.")
    inverted_k = 0
    while k > 0:
        digit = k % 10
        inverted_k = inverted_k * 10 + digit
        k //= 10
    return inverted_k


i = 0
while i < 5:
    while True:
        try:
            a = input("Введите положительное целое число: ")
            a = int(a)
            if a < 0:
                raise ValueError("Неправильно ввели! Число должно быть неотрицательным.")
            break
        except ValueError:
            print("Неправильно ввели! Введите целое неотрицательное число.")


    print(f"Инвертированное число: {invert_digits(a)}")
    i += 1

