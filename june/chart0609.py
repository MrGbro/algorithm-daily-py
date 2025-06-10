from typing import List, Counter


class Solution440:
    def findKthNumber(self, n: int, k: int) -> int:
        cur = 1
        k -= 1
        while k:
            step = self.get_count(cur,n)
            if step<=k:
                k-= step
                cur += 1
            else:
                cur *= 10
                k -= 1
        return cur

    def get_count(self,cur:int,n:int)->int:
        step,first,last = 0,cur,cur
        while step <=n:
            step += min(last,n)-first + 1
            first *= 10
            last = last * 10 + 9
        return step


class Solution1615:
    def masterMind(self, solution: str, guess: str) -> List[int]:
        x = sum(a == b for a, b in zip(solution, guess))
        y = sum((Counter(solution) & Counter(guess)).values())
        return [x, y - x]