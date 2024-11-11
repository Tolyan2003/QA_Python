# создаем класс типа Adress

class Address:

    # Объявляем в классе конструктор
    def __init__(self, index, city, street, house, apartment):
        self.index = index
        self.city = city
        self.street = street
        self.house = house
        self.apartment = apartment