import logging
from typing import List


class Solution0801:
    def waysToStep(self, n: int) -> int:
        if n == 0 or n == 1 or n == 2:
            return 2 if n == 2 else 1
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 3]) % 1_000_000_007
        return dp[n]


class Solution1002:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_map = {}
        res = []
        for s in strs:
            ns = sorted(s)
            idx = dict_map.get(str(ns), -1)
            if idx == -1:
                res.append([s])
                dict_map[str(ns)] = len(res) - 1
            else:
                tmp = res[idx]
                tmp.append(s)
        return res


class Solution1003:
    def search(self, arr: List[int], target: int) -> int:
        pass


class Solution189:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        a = nums[:n - k]
        b = nums[n - k:]
        c = b + a
        for i in range(n):
            nums[i] = c[i]
    def rotate2(self,nums:List[int],k:int)->None:
        def rotate(left:int,right:int):
            if left >= right:
                return
            while left < right:
                nums[left],nums[right] = nums[right],nums[left]
                left += 1
                right -= 1
        n = len(nums)
        k = k % n
        rotate(0,n-1)
        rotate(0,k-1)
        rotate(k,n-1)



class Solution153:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        return nums[l]



inst = Solution189()
inst.rotate([1,2,3,4,5],2)


