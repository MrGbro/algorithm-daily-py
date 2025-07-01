import bisect
import math
from typing import List


class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        min_s = math.inf
        for i,v in enumerate(nums):
            s = 0
            while v != 0:
                s += v % 10
                v //= 10
            if s == i:
                min_s = min(min_s,s)
        return min_s if min_s != math.inf else -1


class Solution2367:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        pass


