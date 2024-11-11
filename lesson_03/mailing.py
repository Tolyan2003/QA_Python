# создаем класс типа Mailing

class Mailing:

    #Объявляем в классе конструктор
    def __init__(self, to_address, from_address, cost, track):
        self.to_address = to_address
        self.from_address = from_address
        self.cost = cost
        self.track = track