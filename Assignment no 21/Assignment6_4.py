import threading
import functools

sum_result = 0
prod_result = 1

def calc_sum(lst):
    global sum_result
    sum_result = sum(lst)

def calc_product(lst):
    global prod_result
    prod_result = functools.reduce(lambda x, y: x*y, lst)

lst = list(map(int, input("Enter list: ").split()))

t1 = threading.Thread(target=calc_sum, args=(lst,))
t2 = threading.Thread(target=calc_product, args=(lst,))

t1.start()
t2.start()

t1.join()
t2.join()

print("Sum of Elements:", sum_result)
print("Product of Elements:", prod_result)
