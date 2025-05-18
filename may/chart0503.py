# 1110 删点成林
from typing import Optional, List

from common.base import TreeNode


class Solution1110:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        def dfs(
                node: Optional[TreeNode], res: List[TreeNode], deleted_set: set[int]
        ) -> Optional[TreeNode]:
            if not node:
                return None
            node.left = dfs(node.left, res, deleted_set)
            node.right = dfs(node.right, res, deleted_set)
            if node.val in deleted_set:
                if node.left:
                    res.append(node.left)
                if node.right:
                    res.append(node.right)
                return None
            return node

        del_set: set[int] = set(to_delete)
        res: List[TreeNode] = []
        node: Optional[TreeNode] = dfs(root, res, del_set)
        if node:
            res.append(node)
        return res
