from functools import cache
from typing import List, Optional

from common.base import TreeNode


# 3375
class Solution3375:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        tree: dict[int, int] = {}
        for v in nums:
            if v not in tree:
                tree[v] = 1
            else:
                tree[v] += 1
        if len(tree) == 0:
            return -1
        it = iter(tree)
        first_key: int = next(it)

        if first_key < k:
            return -1
        elif first_key == k:
            return len(tree) - 1
        else:
            return len(tree)


# 98
class Solution98:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def is_valid(node: Optional[TreeNode],
                     lower: Optional[int] = None,
                     upper: Optional[int] = None) -> bool:
            if node is None:
                return True
            if lower is not None and node.val <= lower:
                return False
            if upper is not None and node.val >= upper:
                return False
            return is_valid(node.left, lower, node.val) and is_valid(node.right, node.val, upper)

        return is_valid(root)


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return None
        if root.val == val:
            return root
        if root.val > val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)


# 450
class Solution450:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def getMin(node: Optional[TreeNode]) -> Optional[TreeNode]:
            while node.left is not None:
                node = node.left
            return node

        if root is None:
            return None
        if root.val == key:
            if root.right is None:
                return root.left
            if root.left is None:
                return root.right
            min_node = getMin(root.right)
            root.val = min_node.val
            root.right = self.deleteNode(root.right, min_node.val)
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
        return root


# 96
class Solution96:
    def numTrees(self, n: int) -> int:
        @cache
        def get_num(l: int, r: int) -> int:
            if l > r:
                return 1
            ans = 0
            for i in range(l, r + 1):
                left = get_num(l, i - 1)
                right = get_num(i + 1, r)
                ans += left * right
            return ans

        return get_num(1, n)


# 95 二叉搜索树
class Solution95:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def generate_trees(start: int, end: int) -> List[Optional[TreeNode]]:
            if start > end:
                return [None]
            ans = []
            for i in range(start, end + 1):
                left_trees = generate_trees(start, i - 1)
                right_trees = generate_trees(i + 1, end)
                for left in left_trees:
                    for right in right_trees:
                        root = TreeNode(i)
                        root.left = left
                        root.right = right
                        ans.append(root)
            return ans

        return generate_trees(1, n)
