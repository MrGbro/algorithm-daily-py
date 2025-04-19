from typing import Optional

from common.base import TreeNode


class Solution3319:
    def kthLargestPerfectSubtree(self, root: Optional[TreeNode], k: int) -> int:
        hs = []

        def dfs(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0
            left_count = dfs(node.left)
            right_count = dfs(node.right)
            if left_count < 0 or left_count != right_count:
                return -1
            hs.append(left_count + 1)
            return left_count + 1

        if k > len(hs):
            return -1
        hs.sort()
        return (1 << hs[-k]) - 1


class Solution1339:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        result: int = 0
        mod: int = 10 ** 9 + 7
        total: int = 0

        def sum(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            left = sum(node.left)
            right = sum(node.right)
            return left + right + node.val

        def dfs(node: Optional[TreeNode]) -> int:
            nonlocal result
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            sv = left + right + node.val
            result = max(result, (total - sv) * sv)
            return sv

        total = sum(root)
        dfs(root)
        return result % mod


class Solution1372:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        max_len: int = 0

        def dfs(node: Optional[TreeNode], direction: int, h: int):
            nonlocal max_len
            if not node:
                return
            max_len = max(max_len, h)
            if direction == 0:
                dfs(node.left, 1, h + 1)
                dfs(node.right, 0, 1)
            else:
                dfs(node.left, 1, 1)
                dfs(node.right, 0, h + 1)

        dfs(root, 0, 0)
        dfs(root, 1, 0)
        return max_len


class Solution1145:
    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:
        def get_sum(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            left = get_sum(node.left)
            right = get_sum(node.right)
            return left + right + 1

        res: bool = False
        total: int = get_sum(root)

        def dfs(node: Optional[TreeNode]) -> int:
            nonlocal res
            if not node:
                return 0

            l = dfs(node.left)
            r = dfs(node.right)
            if node.val == x:
                res = max(l, r, total - l - r - 1) * 2 > n
            return l + r + 1

        dfs(root)
        return res


class Solution572:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def is_same(node: Optional[TreeNode], other: Optional[TreeNode]) -> bool:
            if not node and not other:
                return True
            if not node or not other:
                return False
            return node.val == other.val and is_same(node.left, other.left) and is_same(node.right, other.right)

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot) or is_same(root, subRoot)


class Solution:
    def countPairs(self, root: Optional[TreeNode], distance: int) -> int:
        pass
