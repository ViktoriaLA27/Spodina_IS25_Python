# Из исходного текстового файла (Dostoevsky.txt) выбрать блок информации за 1857 год
# и поместить ее в новый текстовый файл.

import re

with open('Dostoevsky.txt', 'r', encoding='utf-8') as f1:
    text = f1.read()

pattern = r'1857 год\s+(.*?идеала – Христа\.)'
match = re.search(pattern, text, re.DOTALL)

if match:
    block = '1857 год\n' + match.group(1).strip()
    with open('Dostoevsky_1857.txt', 'w', encoding='utf-8') as f2:
        f2.write(block)
    print("Блок за 1857 год сохранён.")
else:
    print("Блок за 1857 год не найден.")