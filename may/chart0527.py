from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def count_at_most_k_odd(arr: List[int], k_val: int) -> int:
            if k_val < 0:
                return 0
            l,odd_cnt,ans =0,0,0
            for r,v in enumerate(arr):
                if v % 2 != 0:
                    odd_cnt += 1
                while odd_cnt > k_val:
                    if arr[l] % 2 != 0:
                        odd_cnt -= 1
                    l += 1
                ans += r-l+1
            return ans
        return count_at_most_k_odd(nums,k)-count_at_most_k_odd(nums,k-1)

class Solution125:
    def isPalindrome(self, s: str) -> bool:
        ns = s.lower()
        n = len(ns)
        l, r = 0, n - 1
        while l < r:
            lm = ord(ns[l])
            rm = ord(ns[r])
            if lm < 65 or 90 < lm < 97 or lm > 122:
                l += 1
                continue
            if rm < 65 or 90 < rm < 97 or rm > 122:
                r -= 1
                continue
            if ns[l] != ns[r]:
                return False
            l += 1
            r -= 1
        return True


