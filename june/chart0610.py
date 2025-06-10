import math
from collections import Counter
from typing import List


class Solution3442:
    def maxDifference(self, s: str) -> int:
        cmap = Counter(s)
        odd, even = 0, math.inf
        for k, v in cmap.items():
            if v % 2 == 0:
                even = min(even, v)
            else:
                odd = max(odd, v)
        return odd - even

inst = Solution3442()
inst.maxDifference("aaaaabbc")


class Solution1618:
    def patternMatching(self, pattern: str, value: str) -> bool:
        def check(la:int,lb:int)->bool:
            i =0
            a,b = "",""
            for c in pattern:
                if c == "a":
                    if a and value[i:i+la] != a:
                        return False
                    a = value[i:i+la]
                    i += la
                else:
                    if b and value[i:i+lb] !=b:
                        return False
                    b = value[i:i+lb]
                    i+=lb
            return a!=b
        n = len(value)
        cnt = Counter(pattern)
        if cnt["a"] == 0:
            return n % cnt["b"] == 0 and value[:n // cnt["b"]]*cnt["b"] == value
        if cnt["b"] == 0:
            return n % cnt["a"] == 0 and value[:n // cnt["a"]] * cnt["a"] == value
        for la in range(n+1):
            if la * cnt["a"] > n:
                break
            lb,mod = divmod(n-la*cnt["a"],cnt["b"])
            if mod == 0 and check(la,lb):
                return True
        return False


class Solution1619:
    def pondSizes(self, land: List[List[int]]) -> List[int]:
        pass


