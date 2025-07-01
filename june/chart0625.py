from typing import List


class Solution007:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def nsum(start:int,n:int,target:int)->List[List[int]]:
            res = []
            if n < 2 or len(nums)-start < n:
                return res
            if n == 2:
                l,r =  start,len(nums)-1
                while l < r:
                    left,right = nums[l],nums[r]
                    s = left + right
                    if s > target:
                        while nums[r] == right and l < r:
                            r -= 1
                    elif s < target:
                        while nums[l] == left and l < r:
                            l += 1
                    else:
                        res.append([left,right])
                        while nums[r] == right and l < r:
                            r -= 1
                        while nums[l] == left and l < r:
                            l += 1
            else:
                l = start
                while l < len(nums):
                    arr = nsum(l+1,n-1,target - nums[l])
                    for it in arr:
                        it.append(nums[l])
                        res.append(it)
                    while l < len(nums)-1 and nums[l] == nums[l+1]:
                        l += 1
                    l += 1
            return res

        nums.sort()
        return nsum(0,3,0)