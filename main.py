import time
import threading

a = list(range(10_000_000))
before = time.time()
sum(a)
print(time.time() - before)

before = time.time()
t1 = threading.Thread(target=sum, args=(a[:5_000_000],))
t2 = threading.Thread(target=sum, args=(a[5_000_000:],))

t1.start()
t2.start()

print(time.time() - before)

