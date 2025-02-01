#  Дан символ C и строка S. Удвоить каждое вхождение символа C в строку S.
S = input("Введите текст: ")
C = input("Введите символ: ")
double_C = ""

for i in S:
  if i == C:
    double_C += C * 2
  else:
    double_C += i

print(double_C)
