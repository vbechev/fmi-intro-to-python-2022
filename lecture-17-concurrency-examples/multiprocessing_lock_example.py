from multiprocessing import Process, Value, Lock


def worker(n, lock):
    # work
    lock.acquire()
    v = n.value
    for x in range(0, 30000):
        x += 2
    n.value = v + 1
    lock.release()
    # twerk successfully


if __name__ == '__main__':
    num = Value('i', 0)
    lock = Lock()
    processes = [Process(target=worker, args=(num, lock)) for i in range(0, 10)]
    for p in processes:
        p.start()
    for p in processes:
        p.join()
    print(num.value)
