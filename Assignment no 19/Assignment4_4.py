
from functools import reduce

def even_square_sum():
    data = [5, 2, 3, 4, 1, 2, 8, 10]
    
    print("Input List =", data)

    fdata = list(filter(lambda n: n % 2 == 0, data))
    print("List after filter =", fdata)

    mdata = list(map(lambda n: n * n, fdata))
    print("List after map =", mdata)

    result = reduce(lambda a, b: a + b, mdata)
    print("Output of reduce =", result)

even_square_sum()
