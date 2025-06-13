# Создайте класс "Автомобиль", который содержит информацию о марке, модели и
# годе выпуска. Создайте класс "Грузовик", который наследуется от класса
# "Автомобиль" и содержит информацию о грузоподъемности. Создайте класс
# "Легковой автомобиль", который наследуется от класса "Автомобиль" и содержит
# информацию о количестве пассажиров

class Avtomobil:
    def __init__(self, marka, model, god_vypuska):
        self.marka = marka
        self.model = model
        self.god_vypuska = god_vypuska

class Gruzovik(Avtomobil):
    def __init__(self, marka, model, god_vypuska, gruzopodemnost):
        super().__init__(marka, model, god_vypuska)
        self.gruzopodemnost = gruzopodemnost

class LegkovoyAvtomobil(Avtomobil):
    def __init__(self, marka, model, god_vypuska, kolichestvo_passazhirov):
        super().__init__(marka, model, god_vypuska)
        self.kolichestvo_passazhirov = kolichestvo_passazhirov