import bisect
import math
from collections import Counter
from typing import List


class WordsFrequency1602:

    def __init__(self, book: List[str]):
        self.counter = Counter(book)

    def get(self, word: str) -> int:
        return self.counter.get(word, 0)


class Solution:
    def intersection(self, start1: List[int], end1: List[int], start2: List[int], end2: List[int]) -> List[float]:
        pass


class Solution1604:
    def tictactoe(self, board: List[str]) -> str:
        n = len(board)
        # 行
        row = [0] * n
        colum = [0] * n
        dg = udg = 0
        has_empty = False
        # 列
        for i, r in enumerate(board):
            for j, c in enumerate(r):
                v = 1 if c == "X" else -1
                if c == " ":
                    has_empty = True
                    v = 0
                row[i] += v
                colum[j] += v
                if i == j:
                    dg += v
                if i + j + 1 == n:
                    udg += v
                if abs(row[i]) == n or abs(colum[j]) == n or abs(dg) == n or abs(udg) == n:
                    return c
        # 对角线
        return "Pending" if has_empty else "Draw"


class Solution1605:
    def trailingZeroes(self, n: int) -> int:
        ans = 0
        while n:
            n //= 5
            ans += n
        return ans


class Solution1606:
    def smallestDifference(self, a: List[int], b: List[int]) -> int:
        a.sort()
        b.sort()
        i, j = 0, 0
        ans = math.inf
        while i < len(a) and j < len(b):
            ans = min(ans, abs(a[i] - b[j]))
            if a[i] < b[j]:
                i += 1
            else:
                j += 1
        return ans

    def smallestDifference2(self, a: List[int], b: List[int]) -> int:
        b.sort()
        n = len(b)
        ans = math.inf
        for v in a:
            j = bisect.bisect_left(b, v)
            if j < n:
                ans = min(ans, abs(b[j] - v))
            if j:
                ans = min(ans, abs(b[j - 1] - v))
        return ans


class Solution1607:
    def maximum(self, a: int, b: int) -> int:
        pass
