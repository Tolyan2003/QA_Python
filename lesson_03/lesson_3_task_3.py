from address import Address
from mailing import Mailing

# Создание экземпляров класса Address
to_address = Address(index="123456", city="Москва", street="Тверская", house=10, apartment=20)
from_address = Address(index="654321", city="Санкт-Петербург", street="Невский проспект", house=15, apartment=30)

# Создание экземпляра класса Mailing
mailing = Mailing(to_address=to_address, from_address=from_address, cost=500, track="ABCD12345")

# Печать информации об отправлении в требуемом формате
print(f"Отправление {mailing.track} из {mailing.from_address.index}, {mailing.from_address.city}, "
      f"{mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.apartment} в "
      f"{mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street}, "
      f"{mailing.to_address.house} - {mailing.to_address.apartment}. Стоимость {mailing.cost} рублей.")