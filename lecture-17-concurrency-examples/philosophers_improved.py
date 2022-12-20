import random
import time
import threading


bathroom = threading.Lock()

class Philosopher(threading.Thread):
    def __init__(self, name):
        super().__init__(); self.name = name

    def log(self, msg):
        print("{0}: {1}".format(self.name, msg))

    def eat(self):
        time.sleep(random.random())

    def ponder(self):
        time.sleep(random.random())

    def refresh(self):
        self.log("Please excuse me...")
        bathroom.acquire()
        self.log("--> (entered the bathroom)")
        time.sleep(random.random())
        bathroom.release()
        self.log("<-- (left the bathroom)")

    def run(self):
        while True:
            self.eat(); self.ponder(); self.refresh()


for number in range(5):
    philosopher = Philosopher(f'Gosho {number}')
    philosopher.start()
