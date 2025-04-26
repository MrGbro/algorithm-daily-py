import os
from collections import deque
from functools import reduce
import common.base as Base


def main():
    print("hello world")


def add(a: int, b: int) -> int:
    return a + b


"""
这是多行注释
"""


class User:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def print_user(self):
        print("name:", self.name, "age:", self.age)


# main run
if __name__ == '__main__':
    main()
    user = User("zhangsan", 18)
    user.print_user()
    cpu_nums = os.cpu_count()
    print("cpu count:", cpu_nums)
    root: Base.TreeNode = Base.TreeNode(1)


def normalize(name: str) -> str:
    return str.upper(name[0:1]) + str.lower(name[1:])


L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


def prod(l: list[int]) -> int:
    return reduce(lambda x, y: x * y, l)


print(prod([3, 5, 7, 9]))


def is_odd(n: int) -> bool:
    return n % 2 == 1


print(list(filter(is_odd, [1, 2, 3, 4, 5, 6])))


def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


def _not_divisible(n):
    return lambda x: x % n > 0


def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)


seq = [4, 2, 1, 46, 5, 6, 7, 8, 9, 0]
x: list[int] = sorted(seq)
print(x)
queue: deque[int] = deque()
queue.appendleft(1)

import os
import multiprocessing


# 子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))


def pool_task():
    p = multiprocessing.Pool(4)
    for i in range(5):
        p.apply_async(run_proc, args=(i,))
    print("waiting for all subprocesses done")
    p.close()
    p.join()
    print("all end")


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = multiprocessing.Process(target=run_proc, args=('test',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')
    pool_task()
