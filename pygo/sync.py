import time
from multiprocessing import Value


class WaitGroup(object):
    def __init__(self):
        self.counter = Value('i', 0)

    def wait(self, interval=0.001):
        while self.counter.value != 0:
            time.sleep(interval)

    def add(self, count):
        with self.counter.get_lock():
            self.counter.value += count

    def done(self):
        with self.counter.get_lock():
            self.counter.value -= 1
