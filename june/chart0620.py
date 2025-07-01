from typing import List, Counter


class SolutionBM49:
    def solve(self, s: str) -> int:
        symbol = []
        record = []
        for v in s:
            pass

class Solution1688:
    def numberOfMatches(self, n: int) -> int:
        m = n
        cnt = 0
        for i in range(m):
            if n <= 1:
                break
            if n % 2 != 0:
                cnt += (n - 1) // 2
                n = 1 + (n - 1) // 2
            else:
                cnt += n // 2
                n = n // 2
        return cnt

# inst = Solution1688()
# inst.numberOfMatches(7)


class Solution3270:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        s1 = str(num1)
        l1 = len(s1)
        s2 = str(num2)
        l2 = len(s2)
        s3 = str(num3)
        l3 = len(s3)
        res = ""
        for i in range(4):
            c1 = '0' if 4-l1 < i else s1[i+l1-4]
            c2 = '0' if 4-l2 < i else s2[i+l2-4]
            c3 = '0' if 4-l3 < i else s3[i+l3-4]
            res += min(c1,c2,c3)
        return int(res)

class Solution1160:
    def countCharacters(self, words: List[str], chars: str) -> int:
        hased = Counter(chars)
        length = 0
        for word in words:
            it = Counter(word)
            is_ok = True
            for k,v in it.items():
                if k not in hased or hased[k] < v:
                    is_ok = False
                    break
            if is_ok:
                length += len(word)
        return length

inst = Solution1160()
length = inst.countCharacters(["cat","bt","hat","tree"],"atach")