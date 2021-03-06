def numbers(n: int):
    print(n)

    if n == 0:
        return

    numbers(n - 1)


# numbers(10)

def fib(n: int) -> int:
    if n < 2:
        return n

    return fib(n - 1) + fib(n - 2)


# print(fib(10))

def power(number: int, n: int) -> int:
    if n < 2:
        return number

    return power(number, n - 1) * power(number, n - 2)


# print(power(5, 3))

def reverse(txt: str) -> str:
    pass


def factorial(n: int) -> int:
    if n == 0:
        return 1

    return n * factorial(n - 1)


# print(factorial(4))

def prime(n: int, k=None) -> bool:
    if not k:
        k = n - 1

    if k == 1 or n == 1:
        return True

    if n % k == 0:
        return False

    return prime(n, k - 1)


# print(prime(7))

def n_sums(n: int) -> list:
    pass


