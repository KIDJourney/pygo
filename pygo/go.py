import logging
from .conf import use_process

if use_process():
    from multiprocessing import Process as Worker
else:
    from threading import Thread as Worker


def go(closure, *args, **kwargs):
    w = Worker(target=closure, args=args, kwargs=kwargs)
    w.start()
