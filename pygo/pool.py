import logging
from .conf import use_process
from multiprocessing import Queue

if use_process():
    from multiprocessing import Process as Worker
else:
    from threading import Thread as Worker
from .conf import get_worker_num

logger = logging.getLogger("pygo.pool")

wp = None


def get_wp():
    global wp
    if wp is None:
        wp = WorkerPool()
    return wp


def do_work(idx, q):
    while True:
        task = q.get(block=True)
        if task is None:
            break
        f, args, kwargs = task
        try:
            f(*args, **kwargs)
        except Exception:
            pass


class WorkerPool:
    def __init__(self):
        self.queue = Queue()
        self.worker_num = get_worker_num()
        self.workers = []

    def start(self):
        self.workers = [Worker(target=do_work, args=(i, self.queue,))
                        for i in range(self.worker_num)]
        for w in self.workers:
            w.start()

    def stop(self):
        self.queue.put(None)
        for i in self.workers:
            i.start()

        self.queue.close()
