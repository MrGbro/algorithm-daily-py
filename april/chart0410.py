from typing import List, Optional

from common.base import TreeNode


# 1317 A Number Without Digit 0
class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for i in range(1, n):
            if '0' not in str(i) and '0' not in str(n - i):
                return [i, n - i]
        return []


# 144 Binary Tree Preorder Traversal
class Solution44:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node: Optional[TreeNode], result: List[int]):
            if node is None:
                return
            result.append(node.val)
            dfs(node.left, result)
            dfs(node.right, result)

        result: List[int] = []
        dfs(root, result)
        return result

    def preorderTraversal2(self, root: Optional[TreeNode]) -> List[int]:
        result: List[int] = []
        if not root:
            return result
        result.append(root.val)
        result.extend(self.preorderTraversal2(root.left))
        result.extend(self.preorderTraversal2(root.right))
        return result


# 96 Unique
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node: Optional[TreeNode], result: List[int]):
            if not node:
                return
            dfs(node.left, result)
            result.append(node.val)
            dfs(node.right, result)

        result: List[int] = []
        dfs(root, result)
        return result

# 145 Binary Tree postorder Traversal
class Solution145:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node: Optional[TreeNode], result: List[int]):
            if not node:
                return
            dfs(node.left, result)
            dfs(node.right, result)
            result.append(node.val)

        result: List[int] = []
        dfs(root, result)
        return result


# 872 Leaf-Similar Trees
class Solution872:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(node: Optional[TreeNode], result: List[int]):
            if not node:
                return
            if not node.left and not node.right:
                result.append(node.val)
            dfs(node.left, result)
            dfs(node.right, result)

        res1: List[int] = []
        res2: List[int] = []
        dfs(root1, res1)
        dfs(root2, res2)
        return res1 == res2

# 44 Number of Different Colors in a Binary Tree
class Solution44:
    def numColor(self, root: TreeNode) -> int:
        def dfs(node: TreeNode, count: set[int]):
            if not node:
                return
            count.add(node.val)
            dfs(node.left, count)
            dfs(node.right, count)

        cnt: set[int] = set()
        dfs(root, cnt)
        return len(cnt)

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        sum :int = 0
        def dfs(node:Optional[TreeNode]):
            nonlocal sum
            if not node:
                return
            if node.left and not node.left.left and not node.left.right:
                sum += node.left.val
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return sum
