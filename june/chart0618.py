import bisect
from collections import defaultdict
from typing import List


class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.array = arr
        self.array.sort()

    def query(self, left: int, right: int, value: int) -> int:
        if len(self.array) <= 0:
            return 0
        l = bisect.bisect_left(self.array,value,left,right)
        r = bisect.bisect_right(self.array,value,left,right)
        return r-l


class Solution3488:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        index = defaultdict(list)
        for i,x in enumerate(nums):
            index[x].append(i)
        n = len(nums)
        for v in index.values():
            s = v[0]
            v.insert(0,v[-1]-n)
            v.append(s + n)
        res = []
        for i,x in enumerate(queries):
            ls = index[nums[x]]
            if len(ls) == 3:
                res.append(-1)
            else:
               j = bisect.bisect_left(ls,x)
               res.append(min(x-ls[j-1],ls[j+1]-x))
        return res


class Solution2070:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        pass

