
from functools import reduce

def list_filter_map_reduce():
    data = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
    
    print("Input List =", data)

    fdata = list(filter(lambda n: n >= 70 and n <= 90, data))
    print("List after filter =", fdata)

    mdata = list(map(lambda n: n + 10, fdata))
    print("List after map =", mdata)

    result = reduce(lambda a, b: a * b, mdata)
    print("Output of reduce =", result)

list_filter_map_reduce()
