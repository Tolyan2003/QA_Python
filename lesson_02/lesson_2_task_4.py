def fizz_buzz (n):
    for i in range(1, n+1):
        if i % 15 == 0:
            print(f"FizzBuzz")
        elif i % 3 == 0:
            print(f"Fizz")
        elif i % 5 == 0:
            print(f"Buzz")
        else:
            print(i)


n = int(input("Введите число: "))
fizz_buzz(n)