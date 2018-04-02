from multiprocessing import cpu_count

USE_PROCESS = True
WORKER_NUM = None


def use_process():
    return USE_PROCESS


def get_worker_num():
    return WORKER_NUM or cpu_count() * 2


def set_use_process(flag):
    if flag:
        USE_PROCESS = True
    else:
        USE_PROCESS = False


def set_worker_num(num):
    try:
        WORKER_NUM = int(num)
    except Exception:
        raise Exception("worker num must be numerical")
