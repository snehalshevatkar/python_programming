# Assignment3_5.py
from functools import reduce

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def prime_double_max():
    data = [2, 70, 11, 10, 17, 23, 31, 77]

    print("Input List =", data)

    fdata = list(filter(is_prime, data))
    print("List after filter =", fdata)

    mdata = list(map(lambda n: n * 2, fdata))
    print("List after map =", mdata)

    result = reduce(lambda a, b: a if a > b else b, mdata)
    print("Output of reduce =", result)

prime_double_max()
