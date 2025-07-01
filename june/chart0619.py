import bisect
from typing import List


class Solution2070:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort(key=lambda x: x[0])
        res = []
        for i in queries:
            idx = bisect.bisect_right(items, i)
            if idx <= 0:
                res.append(0)
            else:
                m = 0
                for j in range(idx):
                    m = max(m, items[j][-1])
                res.append(m)
        return res


class Solution:
    def minNumberDisappeared(self , nums: List[int]) -> int:
        # write code here
        nums.sort()
        mx = nums[-1]
        tmp = [0] * (mx+2)
        for v in nums:
            if v < 0:
                continue
            tmp[v] = 1
        for i,v in enumerate(tmp):
            if v == 0:
                return i
        return None
inst = Solution()
v = inst.minNumberDisappeared([1,0,2])
print(v)