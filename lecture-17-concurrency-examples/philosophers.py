import random
import time
import threading


taken = False

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
        global taken
        self.log("Please excuse me...");
        while taken:
            pass
        taken = True
        self.log("--> (entered the bathroom)")
        time.sleep(random.random())
        taken = False
        self.log("<-- (left the bathroom)")

    def run(self):
        while True:
            self.eat()
            self.ponder()
            self.refresh()


for number in range(5):
    philosopher = Philosopher(f'Gosho {number}')
    philosopher.start()
