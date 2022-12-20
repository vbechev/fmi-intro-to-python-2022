from multiprocessing import Process, Value


def worker(n):
    # work
    v = n.value
    for x in range(0, 30000):
        x += 2
    n.value = v + 1
    # twerk poorly
    # we will probably have a wrong value at the end


if __name__ == '__main__':
    num = Value('i', 0)
    processes = [Process(target=worker, args=(num,)) for i in range(0, 10)]
    for p in processes:
        p.start()
    for p in processes:
        p.join()
    print(num.value)
