from typing import List


class Solution0503:
    def reverseBits(self, num: int) -> int:
        ans,cnt,j = 0,0,0
        for i in range(32):
            cnt += num >> i & 1 ^ 1
            while cnt > 1 and j <=i:
                cnt -= num >> j & 1 ^ 1
                j += 1
            ans = max(ans,i-j+1)
        return ans