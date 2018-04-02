import pytest
import time

import pygo

pygo.init()


def add_number(v, l, wg):
    l.append(v)
    time.sleep(1)
    wg.done()


def test_go():
    l = pygo.list()
    v = 10
    wg = pygo.WaitGroup()
    wg.add(2)

    pygo.go(add_number, v, l, wg)
    pygo.go(add_number, v, l, wg)
    wg.wait()

    assert list(l) == [10, 10]
