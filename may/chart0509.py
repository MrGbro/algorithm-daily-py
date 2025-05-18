import unittest
from bisect import bisect_left
from typing import Optional, List

from common.base import TreeNode


class Solution2467:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        def dfs(node:TreeNode,target:int,res:List[int]):
            if not node:
                return
            dfs(node.left,target,res)
            if node.val <= target:
                res[0] = node.val
            if node.val >= target:
                res[1] = min(node.val,res[1])
            dfs(node.right,target,res)

        result = []
        for i in queries:
            tp = [0,0]
            dfs(root,i,tp)
            result.append(tp)
        return result


class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        arr = []

        def dfs(root):
            if root is None:
                return
            dfs(root.left)
            arr.append(root.val)
            dfs(root.right)

        dfs(root)
        res = []
        for val in queries:
            maxVal, minVal = -1, -1
            index = bisect_left(arr, val)
            if index != len(arr):
                maxVal = arr[index]
                if arr[index] == val:
                    minVal = arr[index]
                    res.append([minVal, maxVal])
                    continue
            if index != 0:
                minVal = arr[index - 1]
            res.append([minVal, maxVal])
        return res

class Solution653:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        arr = []

        def dfs(node: TreeNode):
            if node is None:
                return
            dfs(node.left)
            arr.append(node.val)
            dfs(node.right)

        dfs(root)
        l, r = 0, len(arr) - 1
        while l < r:
            v = arr[l] + arr[r]
            if v == k:
                return True
            elif v < k:
                l += 1
            else:
                r += 1
        return False


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        index_map = {}
        for i,v in enumerate(nums):
            index_map[v] = i
        def get_big(arr,l,r):
            m = -1
            for x in range(l,r+1):
                m = max(m,arr[x])
            return index_map[m]
        def build_tree(arr,l,r):
            if l > r:
                return None
            idx = get_big(arr,l,r)
            root = TreeNode(arr[idx])
            root.left = build_tree(arr,l,idx-1)
            root.right = build_tree(arr,idx+1,r)
            return  root
        return build_tree(nums,0,len(nums)-1)

class Test653(unittest.TestCase):
    def test_case(self):
        arr = [2,3,4,5,6,7]
        k = 9
        l, r = 0, len(arr) - 1
        while l < r:
            v = arr[l] + arr[r]
            if v == k:
                return True
            elif v < k:
                l += 1
            else:
                r += 1
        return False

