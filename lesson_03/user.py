# создаем класс типа User

class User:

    # создаем конструктор
    def __init__(self, first_name, last_name):
        self.First_name = first_name
        self.Last_name = last_name

    # создаем методы по выводу параметров
    def first_name(self):
        return self.First_name

    def last_name(self):
        return self.Last_name

    def full_name(self):
        return f"Имя: {self.First_name}, Фамилия: {self.Last_name}"