import threading

def even_factor(n):
    even_f = []
    for i in range(1, n+1):
        if n % i == 0 and i % 2 == 0:
            even_f.append(i)
    print("Even Factors:", even_f)
    print("Sum of Even Factors:", sum(even_f))

def odd_factor(n):
    odd_f = []
    for i in range(1, n+1):
        if n % i == 0 and i % 2 != 0:
            odd_f.append(i)
    print("Odd Factors:", odd_f)
    print("Sum of Odd Factors:", sum(odd_f))

num = int(input("Enter number: "))

t1 = threading.Thread(target=even_factor, args=(num,))
t2 = threading.Thread(target=odd_factor, args=(num,))

t1.start()
t2.start()

t1.join()
t2.join()

print("Exit from main")
