from typing import Optional, List

from common.base import TreeNode


class CBTInserter:

    def __init__(self, root: Optional[TreeNode]):
        self.q = [] if not root else [root]
        self.root = root if root else None
        while self.q:
            node = self.q[0]
            if not node.left or not node.right:
                break
            node = self.q.pop(0)
            self.q.append(node.left)
            self.q.append(node.right)

    def insert(self, val: int) -> int:
        while self.q:
            node = self.q[0]
            if not node.left:
                node.left = TreeNode(val)
                return node.val
            if not node.right:
                node.right = TreeNode(val)
                return node.val
            node = self.q.pop(0)
            self.q.append(node.left)
            self.q.append(node.right)
        if not self.root:
            self.root = TreeNode(val)
            self.q.append(self.root)
        return None

    def get_root(self) -> Optional[TreeNode]:
        self.root

class Solution958:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        end = False
        q = [root]
        while q:
            sz = len(q)
            for _ in range(sz):
                node = q.pop(0)
                if end and node:
                    return False
                if not node:
                    end = True
                if node:
                    q.append(node.left)
                    q.append(node.right)
        return True


class Solution863:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parent = {}
        res = []
        def find_parent(node:TreeNode):
            if node is None:
                return
            if node.left:
                parent[node.left.val] = node
            if node.right:
                parent[node.right.val] = node
            find_parent(node.left)
            find_parent(node.right)
        def dfs(node:TreeNode,frm:Optional[TreeNode],depth:int,target:int):
            if node is None:
                return
            if depth == target:
                res.append(node.val)
                return
            if node.left is not frm:
                dfs(node.left,node,depth+1,target)
            if node.right is not frm:
                dfs(node.right,node,depth+1,target)
            if parent[node.val] is not frm:
                dfs(parent[node.val],node,depth+1,target)
        find_parent(root)
        dfs(target,None,0,k)
        return res

class Solution662:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = [root]
        wide = 0
        has_node = True
        while q:
            wide = max(wide,len(q))
            sz = len(q)
            for _ in range(sz):
                node = q.pop(0)
                if not node or (not node.left and not node.right):
                    has_node = False
                else:
                    has_node = True
                q.append(node.left if node else None)
                q.append(node.right if node else None)
            if has_node is False:
                break
        return wide



s = [1]
while s:
    print(s.pop(0))
print("loop is over")