# Приложение ИНТЕРНЕТ-МАГАЗИН для некоторой организации. БД должна
# содержать таблицу Продажи со следующей структурой записи: ФИО покупателя, товар,
# единицу измерения (штуки, килограммы, литры), количество, стоимость.
import sqlite3 as sq

with sq.connect('InternetStore.db') as stor:
    cur = stor.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS store 
                    (id_store INTEGER PRIMARY KEY AUTOINCREMENT, 
                    fio_customer TEXT NOT NULL, 
                    items TEXT NOT NULL, 
                    units_measurе TEXT NOT NULL, 
                    quantity INTEGER NOT NULL, 
                    price INTEGER NOT NULL); """)
    stor.commit()

store_list = [
    (1, 'Ермолин Михаил Валерьевич', 'Зубная щетка', 'шт', 4, 100),
    (2, 'Зубнов Александр Мстиславович', 'Мука', 'кг', 2, 160),
    (3, 'Смирнова Анна Петровна', 'Молоко', 'л', 1, 63),
    (4, 'Кузнецов Сергей Владимирович', 'Салфетки', 'шт', 52, 34),
    (5, 'Попов Дмитрий Александрович', 'Резинка для волос', 'шт', 34, 20),
    (6, 'Новикова Мария Сергеевна', 'Батончик протеиновый', 'шт', 12, 70),
    (7, 'Федоров Михаил Григорьевич', 'Грунт садовый', 'кг', 9, 120),
    (8, 'Морозова Ольга Викторовна', 'Очки солнцезащитные', 'шт', 23, 410),
    (9, 'Нестеренко Любовь Андреевна', 'Смартфон', 'шт', 1, 120010)
]
cur.executemany("""INSERT INTO store VALUES (?, ?, ?, ?, ?, ?) """, store_list)

print('\nТовары дороже 100000:')
cur.execute("select * from store where price > 10000")
for row in cur.fetchall():
    print(row)
print('\nТовары количество которых меньше 10:')
cur.execute("select * from store where quantity < 10")
for row in cur.fetchall():
    print(row)
print('\nТовары с единицей измерения - шт:')
cur.execute("select * from store where units_measurе = 'шт'")
for row in cur.fetchall():
    print(row)
print('\nИзменение товара Молоко на Воду.')
cur.execute('update store set items = "Вода питьевая" where items = "Молоко"')
print('\nИзменение единицы измерения на центнеры.')
cur.execute('update store set quantity = "ц" where items = "Грунт садовый"')
print('\nИзменение цены первого товара.')
cur.execute('update store set price = "150" where id_store = 1')
print('\nУдаление товара Солнцезащитные очки.')
cur.execute("delete from store where items = 'Очки солнцезащитные'")
print('\nУдаление товара покупателя Новикова Мария Сергеевна.')
cur.execute("delete from store where fio_customer = 'Новикова Мария Сергеевна'")
print('\nУдаление товара Мука.')
cur.execute("delete from store where items = 'Мука'")


print('\nОбновленная таблица:')
for row in cur.execute('select * from store '):
    print(row)

