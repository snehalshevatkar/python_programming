import threading

def thread1():
    print("Thread1 Started")
    for i in range(1, 51):
        print(i)
    print("Thread1 Completed")

def thread2():
    print("Thread2 Started")
    for i in range(50, 0, -1):
        print(i)
    print("Thread2 Completed")

t1 = threading.Thread(target=thread1)
t2 = threading.Thread(target=thread2)

t1.start()
t1.join()   # Thread2 starts only after Thread1 ends

t2.start()
t2.join()
