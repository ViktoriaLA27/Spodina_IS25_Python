# Организовать словарь на 10 англо-русских слов, обеспечивающий
# "перевод" английского слова на русский.

eng_ru = { "love": "любовь",
           "moon": "луна",
           "door": "дверь",
           "flower": "цветок",
           "man": "мужчина",
           "friend": "друг",
           "surname": "фамилия",
           "bee": "пчела",
           "women": "женщина",
           "song": "песня" }

translate = input("Введите слово на английском языке: ")
if translate in eng_ru:
  print("Перевод: ", eng_ru[translate])
else:
  print("Данного слова нет в словаре.")