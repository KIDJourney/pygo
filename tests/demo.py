import time

from pygo import WaitGroup, go


def test_function(channel, wg):
    time.sleep(10)
    channel.append(100)
    wg.Done()


if __name__ == "__main__":
    wg = WaitGroup()
    wg.add(1)

    res = []
    go(test_function, [], wg)

    wg.wait()

    assert res == [100]
