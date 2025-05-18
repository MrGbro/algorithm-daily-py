from typing import List


class Solution1456:
    def maxVowels(self, s: str, k: int) -> int:
        vowel_cnt = 0
        l = 0
        max_cnt = 0
        for i in range(len(s)):
            val = s[i]
            if self.is_vowel(val):
                vowel_cnt += 1
            while i - l > k - 1:
                d = s[l]
                if self.is_vowel(d):
                    vowel_cnt -= 1
                l += 1
            if i - l + 1 == k:
                max_cnt = max(max_cnt, vowel_cnt)
        return max_cnt

    def is_vowel(self, s: str) -> bool:
        return s == "a" or s == "e" or s == "i" or s == "o" or s == "u"


class Solution634:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum_k = 0
        average: float = -10 ** 9
        l = 0
        if len(nums) < k:
            return sum(nums) / len(nums)
        for i in range(len(nums)):
            v = nums[i]
            sum_k += v
            while i - l > k - 1:
                d = nums[l]
                sum_k -= d
                l += 1
            if i - l == k - 1:
                average = max(average, sum_k / k)
        return average


class Solution1343:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        cnt = 0
        sum_pre = 0
        l = 0
        for i in range(len(arr)):
            sum_pre += arr[i]
            while i - l > k - 1:
                sum_pre -= arr[l]
                l += 1
            if i - l == k - 1:
                average = sum_pre / k
                if average >= threshold:
                    cnt += 1
        return cnt


class Solution2090:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return nums
        if len(nums) < 2 * k:
            return [-1] * len(nums)
        res = [-1] * len(nums)
        sum_pre = 0
        l = 0
        for i in range(len(nums)):
            sum_pre += nums[i]
            while i - l > 2 * k:
                sum_pre -= nums[l]
                l += 1
            if i - l == 2 * k:
                res[(i + l) // 2] = sum_pre // (i - l + 1)
        return res
