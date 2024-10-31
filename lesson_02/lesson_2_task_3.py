import math

def square (side):
    return math.ceil(side ** 2)

side = float(input("Введите сторону квадрата: "))
result = square(side)
print(f"Квадрат со стороной {side} равен {result}")