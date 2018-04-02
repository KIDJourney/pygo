from .sync import WaitGroup
from .go import go
from .conf import set_use_process, set_worker_num
from .container import list


def init(use_process=True, worker_num=None):
    set_use_process(use_process)
    if worker_num:
        set_worker_num(worker_num)
