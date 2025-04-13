from typing import Optional
from typing import List

from common.base import TreeNode


# 1922
class Solution1922:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10 ** 9 + 7
        return pow(5, (n + 1) // 2, mod) * pow(4, n // 2, mod) % mod


class FastMult:
    # 快速求幂
    def pow(self, x: int, y: int):
        ret: int = 1
        mul: int = x
        while y > 0:
            if y % 2 == 1:
                ret *= mul
            mul *= mul
            y //= 2
        return ret


# 1372 交错路径
class Solution1372:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        max_len: int = 0

        def dfs(o: Optional[TreeNode], direction: int, length: int):
            nonlocal max_len
            if not o:
                return

            max_len = max(max_len, length)
            if direction == 0:
                dfs(o.left, 1, length + 1)
                dfs(o.right, 0, 1)
            else:
                dfs(o.right, 0, length + 1)
                dfs(o.left, 1, 1)

        dfs(root, 0, 0)
        dfs(root, 1, 0)
        return max_len


def longest_test(path: List[int]) -> int:
    l: int = 0
    r: int = 1
    last: int = l
    max_len: int = 0
    while r < len(path):
        if path[last] == path[r]:
            l = r
        last = r
        r += 1
        max_len = max(r - l - 1, max_len)
    return max_len


print(longest_test([-1, 1, 0, 0, 1, 0, 1]))


# 971
class Solution(object):
    def flipMatchVoyage(self, root, voyage):
        self.flipped = []
        self.i = 0

        def dfs(node):
            if not node:
                return
            if node.val != voyage[self.i]:
                self.flipped = [-1]
                return
            self.i += 1

            if (self.i < len(voyage) and
                    node.left and node.left.val != voyage[self.i]):
                self.flipped.append(node.val)
                dfs(node.right)
                dfs(node.left)
            else:
                dfs(node.left)
                dfs(node.right)

        dfs(root)
        if self.flipped and self.flipped[0] == -1:
            self.flipped = [-1]
        return self.flipped
