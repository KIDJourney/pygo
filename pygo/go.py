import logging
from .conf import use_process
from .pool import get_wp

if use_process():
    from multiprocessing import Process as Worker
else:
    from threading import Thread as Worker


def go(closure, *args, **kwargs):
    get_wp().put((closure, args, kwargs))
