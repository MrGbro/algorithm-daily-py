from collections import Counter
from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        n = len(matrix)
        m = len(matrix[0])
        self.matrix_sum = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(1,n+1):
            for j in range(1,m+1):
                self.matrix_sum[i][j] = (self.matrix_sum[i-1][j] +
                                         self.matrix_sum[i][j-1] +
                                         matrix[i-1][j-1]-
                                         self.matrix_sum[i-1][j-1])

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.matrix_sum[row2+1][col2+1] - self.matrix_sum[row2+1][col1] - self.matrix_sum[row1][col2+1] + self.matrix_sum[row1][col1]

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)


class Solution014:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need = Counter(s1)
        window = dict()
        l,valid =0,0
        for i,v in enumerate(s2):
            cnt = window.get(v,0)
            window[v] = cnt+1
            if v in need and need.get(v) == window.get(v):
                valid += 1
            while i-l+1 > len(s1):
                d = s2[l]
                if d in need and need[d] == window[d]:
                    valid -= 1
                window[d] = window[d]-1
                l += 1
            if i-l+1 == len(s1) and valid == len(need):
                return True
        return False


class Solution015:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        need = Counter(p)
        window = dict()
        l, valid = 0, 0
        res = []
        for i, v in enumerate(s):
            cnt = window.get(v, 0)
            window[v] = cnt + 1
            if v in need and need.get(v) == window.get(v):
                valid += 1
            while i - l + 1 > len(p):
                d = s[l]
                if d in need and need[d] == window[d]:
                    valid -= 1
                window[d] = window[d] - 1
                l += 1
            if i - l + 1 == len(p) and valid == len(need):
                res.append(l)
        return res

inst = Solution015()
inst.findAnagrams("cbaebabacd","abc")


class Solution018:
    def isPalindrome(self, s: str) -> bool:
        ns = s.lower()
        l,r = 0,len(s)-1
        while l <= r:
            if not s[l].isalpha():
                l += 1
                continue
            if not s[r].isalpha():
                r -= 1
                continue
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

inst = Solution018()
inst.isPalindrome()