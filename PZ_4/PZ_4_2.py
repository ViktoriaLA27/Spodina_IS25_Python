# Дано целое число N (> 1). Вывести наибольшее из целых чисел K, для которых сумма
# 1 + 2 + ... + K будет меньше или равна N, и саму эту сумму.

n = input("Введите целое число N (> 1): ")
while type(n) != int: # обработка исключений
  try:
    n = int(n)

  except ValueError:
    print("Неправильно ввели!")
    n = input("Введите целое число N (> 1): ")
  if n <= 1:
    print("Ошибка: N должно быть больше 1.")
  else:
    k = 0
    summa = 0
  while summa <= n:
    k += 1
    summa += k

    print(f"Наибольшее K: {k - 1}")
    print(f"Сумма: {summa - k}")
