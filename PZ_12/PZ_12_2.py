# Составить генератор (yield), который переведет символы строки из нижнего
# регистра в верхний.

a = input('Введите строку: ')
def upword(A):

  for i in A:
    yield i.upper()

res = "".join(upword(a))

print("Преобразованая строка: ", res)
