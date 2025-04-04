class Solution:
    def scoreOfString(self, s: str) -> int:
        l: int = len(s)
        res: int = 0
        for i in range(l - 1):
            res += abs(ord(s[i])-ord(s[i+1]))
        return res