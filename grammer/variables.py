from typing import List

ls: list[str] = ["a", "b", "c"]

for item in ls:
    print(item)

for i, e in enumerate(ls):
    print(i, e)

print(ls[-1])
print(ls[-2])
print(ls[-3])

simple_map: dict[str, int] = {"a": 1, "b": 2, "c": 3}
print(simple_map['a'])
simple_set: set[str] = {'a', 'b'}
print('a' in simple_set)

# 列表
'''
列表
'''
nums: list[int] = [1, 2, 3]
nums2: list[int] = nums[-3:]

for e in nums2:
    print(e)

rangs: list[int] = list(range(10))
print(len(rangs))

char_map: dict[str, int] = {'a': 1, 'b': 2, 'c': 3}
for k, v in char_map.items():
    print(k, v)

for k in char_map:
    print(k)

tlist: list[tuple[int, int]] = [(1, 2), (3, 4)]
for x, y in tlist:
    print(x, y)


# 7.2
def findMinAndMax(L: list[int]) -> tuple[int, int]:
    minimal: int = None
    maximum: int = None
    if L is not None and len(L) > 0:
        minimal = L[0]
        maximum = L[0]
        for value in L:
            if value < minimal:
                minimal = value
            if value > maximum:
                maximum = value
    return minimal, maximum