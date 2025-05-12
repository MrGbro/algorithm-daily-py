from typing import Optional

from common.base import TreeNode


class Solution1123:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node:TreeNode)->(int,TreeNode):
            if node is None:
                return (0,None)
            lh,lp = dfs(node.left)
            rh,rp = dfs(node.right)
            if lh == rh:
                return lh + 1,node
            if lh > rh:
                return lh + 1,lp
            else:
                return rh + 1,rp
        _,p =dfs(root)
        return p
