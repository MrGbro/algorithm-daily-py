from typing import Optional, List

from common.base import TreeNode


# 1457 伪回文串
class Solution1457:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        count: int = 0

        def is_palindrome(counter: List[int]) -> bool:
            cnt: int = 0
            for v in counter:
                if v % 2 == 1:
                    cnt += 1
            return cnt <= 1

        def dfs(node: Optional[TreeNode], counter: List[int]):
            nonlocal count
            if node is None:
                return
            counter[node.val] += 1
            if node.left is None and node.right is None:
                if is_palindrome(counter):
                    count += 1
            dfs(node.left, counter)
            dfs(node.right, counter)
            counter[node.val] -= 1

        counter = [0] * 10
        dfs(root, counter)
        return count


# 1315 祖父节点值为偶数的节点和
class Solution1315:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        sum: int = 0

        def dfs(cur: Optional[TreeNode],
                parent: Optional[TreeNode] = None,
                grandparent: Optional[TreeNode] = None):
            nonlocal sum
            if not cur:
                return
            if grandparent and grandparent.val % 2 == 0:
                sum += cur.val
            dfs(cur.left, cur, parent)
            dfs(cur.right, cur, parent)

        dfs(root)
        return sum


# 1026 节点与其祖先之间的最大差值
class Solution1026:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(node, mi, ma):
            if not node:
                return 0
            diff = max(abs(node.val - mi), abs(node.val - ma))
            mi = min(mi, node.val)
            ma = max(ma, node.val)
            diff = max(diff, dfs(node.left, mi, ma))
            diff = max(diff, dfs(node.right, mi, ma))
            return diff

        return dfs(root, root.val, root.val)


# 1022 从根到叶的二进制数之和
class Solution1022:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        result: int = 0
        value: int = 0

        def dfs(node: Optional[TreeNode]):
            nonlocal result, value
            if not node:
                return
            value = value * 2 + node.val
            if not node.left and not node.right:
                result += value
            dfs(node.left)
            dfs(node.right)
            value = (value - node.val) // 2

        dfs(root)
        return result


if __name__ == "__main__":
    print(4 / 2)
    print(4 // 2)
