# Создайте класс «Студент», который имеет атрибуты имя, фамилия и оценки.
# Добавьте методы для вычисления среднего балла и определения, является ли студент
# отличником.

class Student:
    def __init__(self, first_name, last_name, otsenki):
        self.first_name = first_name
        self.last_name = last_name
        self.otsenki = otsenki

    def sred_ball(self):
        return sum(self.otsenki) / len(self.otsenki)

    def otlichnik(self):
        return self.sred_ball() > 4.5