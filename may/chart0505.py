from typing import Optional

from common.base import TreeNode


class Solution865:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node: Optional[TreeNode]) -> (int, Optional[TreeNode]):
            if not node:
                return (0, None)
            l, lp = dfs(node.left)
            r, rp = dfs(node.right)
            if l == r:
                return (l + 1, node)
            elif l > r:
                return (l + 1, lp)
            else:
                return (r + 1, rp)

        _, p = dfs(root)
        return p


class Solution1080:
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
        def check_leaf(node: TreeNode, s: int, l: int) -> bool:
            if not node:
                return False
            if not node.left and not node.right:
                return s + node.val >= l
            ml = check_leaf(node.left, s + node.val, l)
            mr = check_leaf(node.right, s + node.val, l)
            if not ml:
                node.left = None
            if not mr:
                node.right = None
            return mr or ml

        if not check_leaf(root, 0, limit):
            return None
        return root


class Solution687:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        max_len: int = 0

        def dfs(node: Optional[TreeNode], parent: int) -> int:
            nonlocal max_len
            if not node:
                return 0
            l = dfs(node.left, node.val)
            r = dfs(node.right, node.val)
            max_len = max(max_len, l + r)
            if node.val != parent:
                return 0
            return max(l, r) + 1

        if not root:
            return max_len
        dfs(root, root.val)
        return max_len
