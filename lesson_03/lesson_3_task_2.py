from smartphone import Smartphone

# создание каталога
catalog = [
    Smartphone("Apple", "iPhone 14 Pro Max", "+79161234567"),
    Smartphone("Samsung", "Galaxy S24 Ultra", "+79212345678"),
    Smartphone("Xiaomi", "Mi 14 Ultra", "+79341234569"),
    Smartphone("Huawei", "P80 Pro", "+79451234670"),
    Smartphone("OnePlus", "11 Pro", "+79561234781")
]
# организация цикла для вывода информации о каждом смартфоне в каталоге в требуемом формате
for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")