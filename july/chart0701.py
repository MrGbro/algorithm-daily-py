from typing import List


class Solution:
    def possibleStringCount(self, word: str) -> int:
        cnt = 1
        start = 0
        batch = 0
        for i in range(len(word)):
            if word[i] == word[start]:
                batch += 1
            else:
                if batch > 1:
                    cnt += batch - 1
                batch = 1
                start = i
        if batch > 1:
            cnt += batch - 1
        return cnt

class Solution33:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        idx_map = dict()
        for i,v in enumerate(order):
            idx_map[v] = i
        for i in range(len(words)-1):
            w1,w2 = words[i],words[i+1]
            length = max(len(w1),len(w2))
            for j in range(length):
                v1,v2 = (
                    -1 if j >= len(w1) else idx_map[w1[j]],
                    -1 if j >= len(w2) else idx_map[w2[j]]
                )
                if v1 > v2:
                    return False
                if v1 < v2:
                    break
        return True

inst = Solution33()
inst.isAlienSorted(["hello","leetcode"],"hlabcdefgijkmnopqrstuvwxyz")