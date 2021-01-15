import random
import threading
import matplotlib.pyplot as plt

bin = []
x = list(range(1, 17))

def thread_task(lock, data):
    lock.acquire()
    a1 = 0
    a2 = 0
    a3 = 0
    a4 = 0
    for i in range(len(data)):
        if data[i] >= 0 and data[i] < 250:
            a1 += 1
        elif data[i] >= 250 and data[i] < 500:
            a2 += 1
        elif data[i] >= 500 and data[i] < 750:
            a3 += 1
        elif data[i] >= 750 and data[i] < 1000:
            a4 += 1

    bin.append(a1)
    bin.append(a2)
    bin.append(a3)
    bin.append(a4)
    lock.release()

data = []

for i in range(1000):
    data.append(random.random() * 1000)

lock = threading.Lock()
threads = []

for i in range(4):
    t = threading.Thread(target=thread_task, args=(lock, data))
    threads.append(t)
    t.start()

for thread in threads:
    thread.join()

barChart = plt.bar(x, bin)
plt.show()