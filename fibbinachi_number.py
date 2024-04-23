""" Формула вычисления числа фибоначчи для Марсохода"""
# a: int = int(input())
a: int = 5
def fibonacci(n):
    if n in (0, 1):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(a))