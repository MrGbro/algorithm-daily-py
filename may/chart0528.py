from bisect import bisect_right, bisect_left
from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def count_k(arr: List[int], kv: int) -> int:
            if kv < 0:
                return 0
            l =0
            cnt =0
            ans = 0
            for r in range(len(arr)):
                if arr[r] % 2 != 0:
                    cnt += 1
                while cnt > kv:
                    if arr[l] % 2 != 0:
                        cnt -= 1
                    l += 1
                ans += r-l +1
            return ans
        return count_k(nums,k)-count_k(nums,k-1)
class Solution658:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        arr.sort(key=lambda a:abs(a-x))
        return arr[:k]


class Solution1471:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        mid = arr[(len(arr) - 1) // 2]
        arr.sort(key=lambda x:abs(x-mid))
        return arr[len(arr)-k:]

class Solution2563:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        ans = 0
        for j, x in enumerate(nums):
            r = bisect_right(nums, upper - x, 0, j)
            l = bisect_left(nums, lower - x, 0, j)
            ans += r - l
        return ans




