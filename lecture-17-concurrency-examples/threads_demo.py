import threading
import time
import random


orders = 0

def log(msg): print("\n* " + msg)

class Chef(threading.Thread):
    def __init__(self, order):
        self.order = order
        threading.Thread.__init__(self)

    def run(self):
        time.sleep(random.randint(1, 5))
        log("Order '{0}' is ready!".format(self.order))


while True:
    order = input('Enter order: ')
    if not order:
        continue
    if order in ('q', 'x', 'quit', 'exit'):
        break
    chef = Chef(order)
    chef.start()
    log("Roger that '{0}'. Please, wait in quiet desperation.".format(order))
    orders += 1
