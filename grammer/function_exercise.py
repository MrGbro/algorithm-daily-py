from functools import reduce
from typing import Callable

add: Callable[[int, int], int] = lambda a, b: a + b
print(add(1, 2))


def add_super(a: int, b: int, func: Callable[[int], int]) -> int:
    return func(a) + func(b)


print(add_super(1, 2, lambda x: x + 1))
res: map = map(lambda x: x + 1, [1, 2, 3, 4, 5])
for re in res:
    print(re)


result:int = reduce(add, [1, 2, 3, 4, 5])
print(result)

result = sum([1, 2, 3, 4, 5])
print(result)