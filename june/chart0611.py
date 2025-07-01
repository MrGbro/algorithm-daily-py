import string
from typing import List


class Solution1620:
    def getValidT9Words(self, num: str, words: List[str]) -> List[str]:
        def check(word: str) -> bool:
            return all(w_map[c] == num[i] for i, c in enumerate(word))

        w_map = {c: d for c, d in zip(string.ascii_lowercase, "22233344455566677778889999")}
        return [w for w in words if check(w)]


class Solution1621:
    def findSwapValues(self, array1: List[int], array2: List[int]) -> List[int]:
        a = sum(array1)
        b = sum(array2)
        s = a + b
        if s % 2 != 0:
            return []
        half = s // 2
        s1 = set(array1)
        s2 = set(array2)
        for v in s1:
            delta = a - v
            rest = half - delta
            if rest in s2:
                return [v, rest]
        return []


class Solution1626:
    def calculate(self, s: str) -> int:
        if not s:
            return 0
        n = len(s)
        x = 0
        sign = '+'
        stk = []
        for i, v in enumerate(s):
            if v.isdigit():
                x = x * 10 + (ord(v) - ord('0'))
            if i == n - 1 or v in '+-*/':
                if sign == '+':
                    stk.append(x)
                elif sign == '-':
                    stk.append(-x)
                elif sign == '*':
                    stk.append(stk.pop() * x)
                else:
                    stk.append(stk.pop() // x)
                x = 0
                sign = v
        return sum(stk)


class Solution1701:
    def add(self, a: int, b: int) -> int:
        carry = 0
        res = 0
        rnd = 0
        while a or b:
            a_ = a & 1
            b_ = b & 1
            carry,rst = divmod(a_+b_+carry,2)
            res = rst << rnd | res
            rnd += 1
            a >>= 1
            b >>= 1
        return res
