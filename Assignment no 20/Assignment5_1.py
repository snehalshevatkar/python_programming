import threading

def even():
    print("Even Thread:")
    for i in range(2, 21, 2):
        print(i)

def odd():
    print("Odd Thread:")
    for i in range(1, 20, 2):
        print(i)

t1 = threading.Thread(target=even, name="Even")
t2 = threading.Thread(target=odd, name="Odd")

t1.start()
t2.start()

t1.join()
t2.join()

print("Main Thread Exit")
