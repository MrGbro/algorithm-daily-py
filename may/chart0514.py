from typing import Optional
from xml.dom.minidom import NamedNodeMap

from common.base import TreeNode


class Solution2415:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = [root]
        odd = False
        while len(q) > 0:
            sz = len(q)
            tmp = []
            for _ in range(sz):
                node = q.pop(0)
                tmp.append(node)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if odd:
                for i in range(len(tmp) // 2):
                    tmp[i].val, tmp[len(tmp) - i - 1].val = tmp[len(tmp) - i - 1].val, tmp[i].val
            odd = not odd
        return root


class Solution1609:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        q = [root]
        even = True
        while len(q) > 0:
            sz = len(q)
            pre = 0 if even else 1_000_001
            for _ in range(sz):
                node = q.pop(0)
                if even:
                    if node.val <= pre or node.val % 2 == 0:
                        return False
                else:
                    if node.val >= pre or node.val % 2 != 0:
                        return False
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            even = not even
        return True


class Solution623:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        q = [root]
        dp = 1
        if depth == 1:
            r = TreeNode(val)
            r.left = root
            return  r
        while len(q) > 0:
            sz = len(q)
            for _ in range(sz):
                node = q.pop(0)
                if depth-1 == dp:
                    l = node.left
                    r = node.right
                    node.left = TreeNode(val,l)
                    node.right = TreeNode(val,None,r)
                else:
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            dp += 1
        return root


class Solution2641:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        root.val = 0
        q = [root]
        while len(q) > 0:
            sz = len(q)
            level_sum = 0
            tmp = []
            for _ in range(sz):
                node = q.pop(0)
                tmp.append(node)
                if node.left:
                    level_sum += node.left.val
                    q.append(node.left)
                if node.right:
                    level_sum += node.right.val
                    q.append(node.right)
            for nd in tmp:
                rest = level_sum
                rest -= 0 if not nd.left else nd.left.val
                rest -= 0 if not nd.right else nd.right.val
                if nd.left:
                    nd.left.val = rest
                if nd.right:
                    nd.right.val = rest
        return root


class CBTInserter:

    def __init__(self, root: Optional[TreeNode]):
        pass

    def insert(self, val: int) -> int:
        pass


class Solution:
    def reverseDegree(self, s: str) -> int:
        res = 0
        for i in s:
            delta = ord(i)-ord('z')
            res += (abs(delta)+1)*(26 + delta)
        return res

