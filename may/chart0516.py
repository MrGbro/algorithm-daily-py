from typing import List, Optional

from common.base import TreeNode


class Solution2901:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(groups)
        dp = [1] * n
        pre_v = [-1] * n
        last = 0
        for i in range(1, n):
            for j in range(i):
                if groups[i] != groups[j] and self.check(words[i], words[j]) and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    pre_v[i] = j
            if dp[i] > dp[last]:
                last = i
        res = []
        while last >= 0:
            res.append(words[last])
            last = pre_v[last]
        res.reverse()
        return res

    def check(self, a: str, b: str) -> bool:
        if len(a) != len(b):
            return False
        diff = 0
        for a1, b1 in zip(a, b):
            if a1 != b1:
                diff += 1
            if diff > 1:
                return False
        return diff == 1


class Solution863:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parent = {}
        res = []

        def find_parent(node: TreeNode):
            if node.left:
                parent[node.left.val] = node
                find_parent(node.left)
            if node.right:
                parent[node.right.val] = node
                find_parent(node.right)

        def find_dist_k(node: Optional[TreeNode], frm: Optional[TreeNode], depth: int, tar: int):
            if not node:
                return
            if depth == tar:
                res.append(node.val)
                return
            if node.left != frm:
                find_dist_k(node.left, node, depth + 1, tar)
            if node.right != frm:
                find_dist_k(node.right, node, depth + 1, tar)
            if parent.get(node.val) != frm:
                find_dist_k(parent.get(node.val), node, depth + 1, tar)

        find_parent(root)
        find_dist_k(target, None, 0, k)
        return res


class Solution662:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = [[root, 1]]
        res = 1
        while q:
            sz = len(q)
            for _ in range(sz):
                node = q.pop(0)
                if node[0].left:
                    q.append([node[0].left, node[1] * 2])
                if node[0].right:
                    q.append([node[0].right, node[1] * 2 + 1])
            res = max(res, q[-1][1] - q[0][1])
        return res


class Solution114:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        self.flatten(root.left)
        self.flatten(root.right)
        right = root.right
        left = root.left
        root.left = None
        root.right = left
        p = root
        while p.right:
            p = p.right
        p.right = right


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution1367:
    def dfs(self, head: ListNode, root: TreeNode):
        if not head:
            return True
        if not root:
            return False
        if head.val != root.val:
            return False
        return self.dfs(head.next, root.left) or self.dfs(head.next, root.right)

    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        return self.dfs(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)
