from typing import List


class Solution2461:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        cnt_map = {}
        l = 0
        sum_pre = 0
        max_sum = 0
        for i in range(len(nums)):
            sum_pre += nums[i]
            cnt_map[nums[i]] = cnt_map.get(nums[i], 0) + 1
            while i - l > k - 1:
                sum_pre -= nums[l]
                cnt_map[nums[l]] = cnt_map[nums[l]] - 1
                if cnt_map[nums[l]] == 0:
                    del cnt_map[nums[l]]
                l += 1
            if i - l == k - 1 and len(cnt_map) == k:
                max_sum = max(max_sum, sum_pre)
        return max_sum

class Solution1423:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        sum_pre = 0
        max_sum = 0
        length = len(cardPoints)
        l = 0
        for i in range(length + k):
            sum_pre += cardPoints[i % length]
            if i - l == k - 1:
                if l >= length-k:
                    max_sum = max(max_sum, sum_pre)
                sum_pre -= cardPoints[l % length]
                l += 1
        return max_sum

class Solution1652:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        pass