from math import inf
from typing import List


class Solution15:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def nsum(arr: List[int], start: int, n: int, target: int) -> List[List[int]]:
            res = []
            if n < 2 or len(arr) - start < n:
                return res
            if n == 2:
                l, r = start, len(arr) - 1
                while l < r:
                    lv, rv = arr[l], arr[r]
                    s = lv + rv
                    if s > target:
                        while l < r and arr[r] == rv:
                            r -= 1
                    elif s < target:
                        while l < r and arr[l] == lv:
                            l += 1
                    else:
                        tmp = [lv, rv]
                        res.append(tmp)
                        while l < r and arr[r] == rv:
                            r -= 1
                        while l < r and arr[l] == lv:
                            l += 1
            else:
                l = start
                while l < len(arr):
                    ns = nsum(arr, l + 1, n - 1, target - arr[l])
                    for tm in ns:
                        tm.append(nums[l])
                        res.append(tm)
                    while l < len(arr) - 1 and arr[l] == arr[l + 1]:
                        l += 1
                    l += 1
            return res

        nums.sort()
        return nsum(nums, 0, 3, 0)


class Solution611:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        cnt = 0
        for i in range(2, len(nums)):
            l, r, c = 0, i - 1, nums[i]
            while l < r:
                if nums[l] + nums[r] > c:
                    cnt += r - l
                    r -= 1
                else:
                    l += 1
        return cnt


class Solution16:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        def find_two(arr: List[int], start: int, tar: int) -> int:
            l, r = start, len(arr) - 1
            delt = inf
            while l < r:
                s = arr[l] + arr[r]
                if abs(delt) > abs(tar - s):
                    delt = tar - s
                if s < tar:
                    l += 1
                else:
                    r -= 1
            return tar - delt

        nums.sort()
        n = len(nums)
        delta = inf
        for i in range(n):
            s = nums[i] + find_two(nums, i + 1, target - nums[i])
            if abs(delta) > abs(target - s):
                delta = target - s
        return target - delta


class Solution18:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def nsun(arr: List[int], start: int, n: int, t: int) -> List[List[int]]:
            res = []
            if n < 2 or len(arr) - start < n:
                return res
            if n == 2:
                l, r = start, len(arr) - 1
                while l < r:
                    lv, rv = arr[l], arr[r]
                    s = lv + rv
                    if s> t:
                        while l < r and arr[r] == rv:
                            r -= 1
                    elif s < t:
                        while l < r and arr[l] == lv:
                            l += 1
                    else:
                        tmp = [lv, rv]
                        res.append(tmp)
                        while l < r and arr[r] == rv:
                            r -= 1
                        while l < r and arr[l] == lv:
                            l += 1
            else:
                i = start
                while i < len(arr):
                    ns = nsun(arr,i+1,n-1,t-arr[i])
                    for it in ns:
                        it.append(arr[i])
                        res.append(it)
                    while i < len(arr)-1 and arr[i] == arr[i+1]:
                        i += 1
                    i += 1
            return res
        nums.sort()
        return nsun(nums, 0, 4, target)


class Solution1577:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        cnt:int = 0
        
        return cnt
