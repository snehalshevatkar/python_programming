import threading

def even_list(lst):
    ev = [x for x in lst if x % 2 == 0]
    print("Even List:", ev)
    print("Sum of Even List:", sum(ev))

def odd_list(lst):
    od = [x for x in lst if x % 2 != 0]
    print("Odd List:", od)
    print("Sum of Odd List:", sum(od))

lst = list(map(int, input("Enter numbers: ").split()))

t1 = threading.Thread(target=even_list, args=(lst,))
t2 = threading.Thread(target=odd_list, args=(lst,))

t1.start()
t2.start()

t1.join()
t2.join()
