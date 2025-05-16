from collections import deque
from typing import Optional, List

from common.base import TreeNode


class Solution103:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        queue = deque()
        if root:
            queue.append(root)
        while len(queue) > 0:
            sz = len(queue)
            tmp = []
            for _ in range(sz):
                node = queue.pop()
                tmp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(tmp)
        return res
