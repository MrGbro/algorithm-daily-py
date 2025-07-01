import bisect
from typing import List


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        res = []
        potions.sort()
        n = len(potions)
        for i in spells:
            l = bisect.bisect_right(potions,success // i,0,n-1)
            res.append(n-l)
        return res


class Solution1385:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        res = 0
        arr2.sort()
        n = len(arr2)
        for i in arr1:
            l = bisect.bisect_left(arr2,i)
            r = bisect.bisect_right(arr2,i)
            if l != r:
                continue
            if l >= n:
                res += 1 if abs(i-arr2[l-1]) <=d else 0
                continue
            if abs(i-arr2[l]) > d or (l+1<n and abs(arr2[l+1]-i) > d):
                continue
            res += 1
        return res


class Solution2389:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        sums = [nums[0]]
        for i in range(1,len(nums)):
            sums.append(sums[-1]+nums[i])
        res = [0] * len(queries)
        for j in queries:
            l = bisect.bisect_left(sums,j)
            res.append(l)
        return res


class Solution1170:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        pass



