from typing import Generator, Any

ls: list[int] = list(range(1, 11))
print(ls)

# 迭代式
ls = [x * x for x in range(1, 11) if x % 2 == 0]
print(ls)

alist = [m + n for m in 'ABC' for n in 'XYZ']
print(alist)

d: dict[str:int] = {'a': 1, 'b': 2, 'c': 3}
dls: list[str] = [k + '=' + str(v) for k, v in d.items()]
print(dls)

g: Generator[int, None, None] = (x * x for x in range(10))
for e in g:
    print(e)


def fib(max: int) -> Generator[int, None, str]:
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n += 1
    return 'done'

for e in fib(6):
    print(e)

def pascal_triangle():
    row = [1]
    while True:
        yield row
        row = [x + y for x, y in zip([0] + row, row + [0])]

def pascal_triangle2(n :int)->Generator[list[int], None, None]:
    row = [1]
    for i in range(n):
        yield row
        row = [x + y for x, y in zip([0] + row, row + [0])]


for row in pascal_triangle2(10):
    print(row)

