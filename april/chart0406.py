from operator import ifloordiv
from typing import List, Optional

from common.base import TreeNode


# 368 乘积小于 K 的最大子集
class Solution368:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        dp: List[int] = [0] * len(nums)
        pre: List[int] = [-1] * len(nums)
        for i in range(len(nums)):
            dp[i] = 1
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[j] > dp[i]:
                    dp[i] = dp[j]
                    pre[i] = j
            dp[i] += 1
        max_len: int = 0
        max_idx: int = -1
        for i in range(len(nums)):
            if dp[i] > max_len:
                max_len = dp[i]
                max_idx = i
        res: List[int] = []
        while max_idx != -1:
            res.append(nums[max_idx])
            max_idx = pre[max_idx]
        return res


# 297 二叉树的序列化和反序列化
class Codec297:

    def serialize(self, root: Optional[TreeNode]):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        def dfs(node: Optional[TreeNode]):
            if not node:
                return "null"
            return str(node.val) + "," + dfs(node.left) + "," + dfs(node.right)

        if not root:
            return ""
        return dfs(root)

    def deserialize(self, data: str):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        def dfs(ls: List[str]):
            if not data:
                return None
            if ls[0] == "null":
                ls.pop(0)
                return None
            root: TreeNode = TreeNode(int(ls.pop(0)))
            root.left = dfs(ls)
            root.right = dfs(ls)
            return root

        return dfs(data.split(","))


# 191 位置 1 的个数
class Solution191:
    @staticmethod
    def hamming_weight(self, n: int) -> int:
        cnt: int = 0
        while n:
            cnt += n & 1
            n = n >> 1
        return cnt


# BM 35 判断一棵树是否为完全二叉树
class SolutionBM35:
    def isCompleteTree(self, root: TreeNode) -> bool:
        if not root:
            return True
        queue: List[TreeNode] = [root]
        end: bool = False
        while queue:
            sz: int = len(queue)
            for i in range(sz):
                node: TreeNode = queue.pop(0)
                if end:
                    if node:
                        return False
                else:
                    if not node:
                        end = True
                    else:
                        queue.append(node.left)
                        queue.append(node.right)
        return True


# write code here
# BM 36 判断一棵树是否为平衡二叉树
class SolutionBM36:
    def IsBalanced_Solution(self, pRoot: TreeNode) -> bool:
        if not pRoot:
            return True
        return abs(self.get_height(pRoot.left) - self.get_height(pRoot.right)) <= 1 and self.IsBalanced_Solution(
            pRoot.left) and self.IsBalanced_Solution(pRoot.right)

    def get_height(self, root: TreeNode) -> int:
        if not root:
            return 0
        return max(self.get_height(root.left), self.get_height(root.right)) + 1


# BM 37 二叉树的最近公共祖先
class SolutionBM37:
    def lowestCommonAncestor(self, root: TreeNode, p: int, q: int) -> int:
        cur: TreeNode = root
        while cur:
            if p < cur.val and q < cur.val:
                cur = cur.left
            elif p > cur.val and q > cur.val:
                cur = cur.right
            else:
                return cur.val


# BM 38 二叉树的最近公共祖先
class SolutionBM38:
    def lowestCommonAncestor(self, root: TreeNode, o1: int, o2: int) -> int:
        def dfs(node: TreeNode, parent: int, par_map: dict[int, int]):
            if not node:
                return
            par_map[node.val] = parent
            dfs(node.left, node.val, par_map)
            dfs(node.right, node.val, par_map)

        def find_path(par_map: dict[int, int], target: int) -> List[int]:
            path: List[int] = []
            while target != -1:
                path.append(target)
                target = par_map[target]
            return path

        parent_dict: dict[int, int] = {}
        dfs(root, -1, parent_dict)
        path1: List[int] = find_path(parent_dict, o1)
        path2: List[int] = find_path(parent_dict, o2)
        p_set = set(path2)
        for v in path1:
            if v in p_set:
                return v
        return root.val
