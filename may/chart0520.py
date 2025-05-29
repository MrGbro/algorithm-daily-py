from typing import List


class Solution:
    def maxSatisfied(
        self, customers: List[int], grumpy: List[int], minutes: int
    ) -> int:
        sum_pre = 0
        for i in range(len(customers)):
            if grumpy[i] == 0:
                sum_pre += customers[i]
        l = 0
        max_sum = 0
        for i in range(len(grumpy)):
            if grumpy[i] == 1:
                sum_pre += customers[i]
            if i-l == minutes-1:
                max_sum = max(max_sum,sum_pre)
                if grumpy[l]==1:
                    sum_pre -= customers[l]
                l += 1
        return max_sum

class Solution1652:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        if k == 0:
            return [0] * n
        code2 = [0] * 2* n
        for i in range(2*n):
            code2[i] = code[i % n]
        l = 1 if k > 0 else n+k
        r = k if k > 0 else n-1
        sum_range = 0
        for i in range(l,r+1):
            sum_range += code[i]
        res = [0] * n
        for i in range(n):
            res[i] = sum_range
            sum_range -= code2[l]
            sum_range += code2[r+1]
            l += 1
            r += 1
        return res