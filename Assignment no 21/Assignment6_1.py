import threading

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def prime_list(lst):
    primes = [x for x in lst if is_prime(x)]
    print("Prime Numbers:", primes)

def nonprime_list(lst):
    nonprimes = [x for x in lst if not is_prime(x)]
    print("Non-Prime Numbers:", nonprimes)

lst = list(map(int, input("Enter list: ").split()))

t1 = threading.Thread(target=prime_list, args=(lst,))
t2 = threading.Thread(target=nonprime_list, args=(lst,))

t1.start()
t2.start()

t1.join()
t2.join()
