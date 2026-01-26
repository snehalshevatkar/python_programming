import threading

def small_chars(s):
    count = sum(1 for c in s if c.islower())
    print("Thread Name:", threading.current_thread().name)
    print("Lowercase Count:", count)

def capital_chars(s):
    count = sum(1 for c in s if c.isupper())
    print("Thread Name:", threading.current_thread().name)
    print("Uppercase Count:", count)

def digit_chars(s):
    count = sum(1 for c in s if c.isdigit())
    print("Thread Name:", threading.current_thread().name)
    print("Digit Count:", count)

s = input("Enter String: ")

t1 = threading.Thread(target=small_chars, args=(s,), name="Small")
t2 = threading.Thread(target=capital_chars, args=(s,), name="Capital")
t3 = threading.Thread(target=digit_chars, args=(s,), name="Digits")

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()
