import bisect
from collections import Counter
from typing import List


class Solution189:
    def rotate(self, nums: List[int], k: int) -> None:
        def rotate(l:int,r:int)->None:
            if l > r:
                return
            while l < r:
                nums[l],nums[r] = nums[r],nums[l]
                l += 1
                r -= 1
        n = len(nums)
        k = k % n
        rotate(0,n-1)
        rotate(0,k-1)
        rotate(k,n-1)

class Solution153:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l,r = 0,n-1
        while l < r:
            mid = (l+r) //2
            t = nums[mid]
            if t > nums[r]:
                l = mid + 1
            else:
                r = mid
        return nums[l]

class Solution154:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l,r = 0,n-1
        while l < r:
            mid = (l+r)//2
            t = nums[mid]
            if t > nums[r]:
                l = mid+1
            elif t < nums[r]:
                r = mid
            else:
                r -= 1
        return nums[l]

class Solution33:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l,r = 0,n-1
        while l <=r:
            mid = (l + r) // 2
            t = nums[mid]
            if t == target:
                return mid
            if nums[0] < nums[mid]:
                if nums[0] <= target < nums[target]:
                    r = mid-1
                else:
                    l = mid+1
            else:
                if nums[mid] < target <= nums[n-1]:
                    l = mid+1
                else:
                    r = mid-1
        return -1
class Solution81:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l,r = 0,n-1
        while l <= r:
            while l < r and nums[l] == nums[l+1]:
                l += 1
            while l < r and nums[r] == nums[r-1]:
                r -= 1
            mid = (l+r) // 2
            t = nums[mid]
            if t == target:
                return True
            if nums[0] <= t:
                if nums[0] <= target < t:
                    r = mid-1
                else:
                    l = mid + 1
            else:
                if t < target <= nums[n-1]:
                    l = mid+1
                else:
                    r = mid-1
        return False


class Solution1005:
    def findString(self, words: List[str], s: str) -> int:
        def dfs(i: int, j: int) -> int:
            if i > j:
                return -1
            mid = (i + j) >> 1
            l = dfs(i, mid - 1)
            if l != -1:
                return l
            if words[mid] == s:
                return mid
            return dfs(mid + 1, j)
        return dfs(0, len(words) - 1)

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        y = len(matrix[0])
        for arr in matrix:
            if arr[0] > target or arr[y-1] < target:
                continue
            v = bisect.bisect_left(arr,target)
            if v < y and arr[v] == target:
                return True
        return False
    def searchMatrix2(self,matrix:List[List[int]],target:int)->bool:
        return False