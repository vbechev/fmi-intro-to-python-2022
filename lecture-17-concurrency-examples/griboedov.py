import random
import time
import threading


ovens = threading.Semaphore(5)

class WaiterChef(threading.Thread):
    def __init__(self, name):
        super(WaiterChef, self).__init__()
        self.name = name

    def run(self):
        while True:
            print("...({0}) waiting for an oven".format(self.name))
            ovens.acquire()
            print("--> ({0}) Cooking...".format(self.name))
            time.sleep(random.random() * 10)
            ovens.release()
            print("<-- ({0}) Serving...".format(self.name))
            time.sleep(random.random() * 4)


for _ in range(0, 10):
    WaiterChef(_).start()
