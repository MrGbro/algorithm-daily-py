from typing import List, OrderedDict


class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        window = OrderedDict()
        l, ans = 0, 0
        for r, v in enumerate(nums):
            window[v] = window.get(v,0)+1
            while len(window) >=2 and abs(window.keys()[-1]-window.keys()[0])>2 and l <=r:
                d = nums[l]
                window[d] -= 1
                if window[d] == 0:
                    del window[d]
            ans += r-l + 1
        return ans

s = Solution()
s.continuousSubarrays([5,4,2,4])

