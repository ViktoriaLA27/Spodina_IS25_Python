#  С начала суток прошло N секунд (N - целое). Найти количество секунд, прошедших с начала последней минуты.
 # вводим переменную, обозн-ую кол-во секунд с начала суток

second = input('Введите количество секунд, прошедших с начала суток - ')

while type(second) != int: # обработка исключений
  try:
    second = int(second)
  except ValueError:
    print("Неправильно ввели!")
    second = input("Введите количество секунд, прошедших с начала суток - ")

number_of_second = second % 60
print("Количество секунд, прошедших с начала суток -", number_of_second)
