import threading

counter = 0
lock = threading.Lock()

def increment():
    global counter
    for i in range(5):
        lock.acquire()
        counter += 1
        lock.release()

threads = []

for i in range(3):   # 3 Threads
    t = threading.Thread(target=increment)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("Final Counter Value:", counter)
