class Solution0501:
    def insertBits(self, N: int, M: int, i: int, j: int) -> int:
        for k in range(i, j + 1):
            N &= ~(1 << k)
        return N | M << i
from linecache import cache
from typing import Optional

from common.base import TreeNode


class Solution:
    def checkSubTree(self, t1: Optional[TreeNode], t2: Optional[TreeNode]) -> bool:
        def is_same(tr1,tr2):
            if not tr1 and not tr2:
                return True
            if not tr1 or not tr2:
                return False
            return tr1.val == tr2.val and is_same(tr1.left,tr2.left) and is_same(tr1.right,tr2.right)
        if not t2:
            return True
        if not t1:
            return False
        return is_same(t1,t2) or self.checkSubTree(t1.left,t2) or self.checkSubTree(t1.right,t2)

class Solution0412:
    def pathSum(self, root: Optional[TreeNode], sum: int) -> int:
        def dfs(node,s)->int:
            if not node:
                return 0
            ret = 0
            if node.val == s and not node.left and not node.right:
                ret += 1
            ret += dfs(node.left,s-node.val)
            ret += dfs(node.right,s-node.val)
            return ret
        if not root:
            return 0
        ret = dfs(root,sum)
        ret += self.pathSum(root.left,sum)
        ret += self.pathSum(root.right,sum)
        return ret

