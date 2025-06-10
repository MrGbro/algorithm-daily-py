from collections import deque
from typing import List, Optional

from common.base import TreeNode, ListNode


class Solution0401:
    def findWhetherExistsPath(self, n: int, graph: List[List[int]], start: int, target: int) -> bool:
        def dfs(i: int):
            if i == target:
                return True
            if i in vis:
                return False
            vis.add(i)
            return any(dfs(j) for j in g[i])

        g = [[] for _ in range(n)]
        for a, b in graph:
            g[a].append(b)
        vis = set()
        return dfs(start)


class Solution0402:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def build_tree(arr: List[int], l: int, r: int) -> Optional[TreeNode]:
            if l > r:
                return None
            mid = (l + r) // 2
            root = TreeNode(arr[mid])
            root.left = build_tree(arr, l, mid - 1)
            root.right = build_tree(arr, mid + 1, r)
            return root

        return build_tree(nums, 0, len(nums) - 1)


class Solution0403:
    def listOfDepth(self, tree: Optional[TreeNode]) -> List[Optional[ListNode]]:
        q = deque()
        if tree:
            q.append(tree)
        res = []
        while q:
            sz = len(q)
            dummy = ListNode(-1)
            cur = dummy
            for _ in range(sz):
                node = q.popleft()
                cur.next = ListNode(node.val)
                cur = cur.next
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(dummy.next)
        return res


class Solution0404:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def depth(p: Optional[TreeNode]) -> int:
            if not p:
                return 0
            l = depth(p.left)
            r = depth(p.right)
            return max(l, r) + 1

        if not root:
            return True
        l_dep = depth(root.left)
        r_dep = depth(root.right)
        return abs(l_dep - r_dep) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)


class Solution0405:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def is_valid(node: Optional[TreeNode], max_node: Optional[TreeNode], min_node: Optional[TreeNode]) -> bool:
            if not node:
                return True
            res = True
            if max_node:
                res = res and node.val < max_node.val
            if min_node:
                res = res and node.val > min_node.val
            return res and is_valid(node.left, node, min_node) and is_valid(node.right, max_node, node)

        if not root:
            return True
        return is_valid(root.left, root, None) and is_valid(root.right, None, root)


class Solution0406:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        ls = []

        def inorder(par: Optional[TreeNode]):
            if not par:
                return
            inorder(par.left)
            ls.append(par)
            inorder(par.right)

        inorder(root)
        idx = -1
        for i, v in enumerate(ls):
            if v == p:
                idx = i
                break
        if idx == -1 or idx == len(ls) - 1:
            return None
        return ls[idx + 1]


class Solution0408:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        par = {}

        def dfs(node: Optional[TreeNode]):
            if not node:
                return
            if node.left:
                par[node.left.val] = node
            if node.right:
                par[node.right.val] = node
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        path_p = set()
        path_p.add(p)
        while p:
            p = par.get(p.val)
            if p:
                path_p.add(p)
            else:
                break
        if q in path_p:
            return q
        while q:
            q = par.get(q.val)
            if q:
                if q in path_p:
                    return q
            else:
                break
        return None

    def lowestCommonAncestor2(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root is None or root in [p, q]:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        return root if left and right else left or right


class Solution0409:
    def BSTSequences(self, root: Optional[TreeNode]) -> List[List[int]]:
        pass


class Solution0410:
    def checkSubTree(self, t1: Optional[TreeNode], t2: Optional[TreeNode]) -> bool:
        def is_equal(node: Optional[TreeNode], other: Optional[TreeNode]) -> bool:
            if not node and not other:
                return True
            if not node:
                return False
            if not other:
                return False
            return node.val == other.val and is_equal(node.left, other.left) and is_equal(node.right, other.right)

        return is_equal(t1, t2) or self.checkSubTree(t1.left if t1 else None, t2) or self.checkSubTree(t1.right if t1
                                                                                                       else None, t2)
