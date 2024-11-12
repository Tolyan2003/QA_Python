from user import User

# Создание экземпляра класса User
my_name = User('Петр','Иванов')

print(my_name.first_name())
print(my_name.last_name())
print(my_name.full_name())