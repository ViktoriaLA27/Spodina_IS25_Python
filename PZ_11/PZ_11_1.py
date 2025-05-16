# Средствами языка Python сформировать два текстовых файла (.txt), содержащих по одной
# последовательности из целых положительных и отрицательных чисел. Сформировать
# новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
# обработку элементов:
# Элементы первого и второго файлов:
# Элементы первого файла, присутствующие во втором:
# Элементы второго файла, присутствующие в первом:
# Количество элементов:
# Количество отрицательных элементов:
# Количество положительных элементов:


a = ['2 52 -17 34 -98 61 -8']
f1 = open('data_1.txt', 'w')
f1.writelines(a)
f1.close()

b = ['4 27 84 -26 -8 75 52']
f2 = open('data_2.txt', 'w')
f2.writelines(b)
f2.close()


f3 = open('data_3.txt', 'w', encoding='UTF-8')
f3.write('Элементы первого файла: ')
f3.write('\n')
f3.writelines(a)
f3.write('\n')
f3.write('Элементы второго файла:')
f3.write('\n')
f3.writelines(b)
f3.write('\n')
f3.close()



f4 = open('data_1.txt')
el = f4.read()
el = el.split()
for i in range(len(el)):
    el[i] = int(el[i])
f4.close()

f2 = open('data_2.txt')
el2 = f2.read()
el2 = el2.split()
for i in range(len(el2)):
    el2[i] = int(el2[i])
f2.close()

f3 = open('data_3.txt', 'a', encoding='UTF-8')
f3.write('\n')
f3.write('Количество элементов первого файла: ')
f3.write('\n')
print(len(el), file=f3)
f3.write('Количество элементов второго файла: ')
f3.write('\n')
print(len(el2), file=f3)
f3.close()

f4 = open('data_1.txt', )
f4 = f4.read()
a1 = []
for i in el:
     if i in el2:
        if el not in el2:
            a1.append(i)
a2 = []
for i in el2:
     if i in el:
        if el2 not in el:
            a2.append(i)


f4 = open('data_3.txt', 'a', encoding='UTF-8') # открываем файл для дозаписи
f4.write('\n')
print('Элементы первого файла, присутствующие во втором: ', a1,
      'Элементы второго файла, присутствующие в первом: ', a2, file=f4, sep='\n')
f4.close()

f4 = open('data_1.txt', )
f4 = f4.read()
p, t = 0, 0
for i in range(len(el)):
     if el[i] < 0:
        t += 1
     else:
        p += 1
f4 = open('data_3.txt', 'a', encoding='UTF-8') # открываем файл для дозаписи
f4.write('\n')
print('Количество отрицательных элементов первого файла: ', t,
      'Количество положительных элементов первого файла: ', p, file=f4, sep='\n')
f4.close()

f5 = open('data_2.txt', )
f5 = f5.read()
p, t = 0, 0
for i in range(len(el2)):
     if el2[i] < 0:
        t += 1
     else:
        p += 1
f5 = open('data_3.txt', 'a', encoding='UTF-8') # открываем файл для дозаписи
f5.write('\n')
print('Количество отрицательных элементов второго файла: ', t,
      'Количество положительных элементов второго файла: ', p, file=f5, sep='\n')
f5.close()