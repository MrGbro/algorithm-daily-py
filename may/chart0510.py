import bisect
from typing import List, Optional

from common.base import TreeNode


class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        sum1 = sum2 = 0
        zero1 = zero2 = 0

        for i in nums1:
            sum1 += i
            if i == 0:
                sum1 += 1
                zero1 += 1

        for i in nums2:
            sum2 += i
            if i == 0:
                sum2 += 1
                zero2 += 1

        if (zero1 == 0 and sum2 > sum1) or (zero2 == 0 and sum1 > sum2):
            return -1

        return max(sum1, sum2)


slon = Solution()
print(slon.minSum([3, 2, 0, 1, 0], [6, 5, 0]))


class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        arr: List[int] = []

        def inorder(node: Optional[TreeNode]):
            if node is None:
                return
            inorder(node.left)
            arr.append(node.val)
            inorder(node.right)

        inorder(root)
        res: List[List[int]] = []
        for val in queries:
            minVal, maxVal = -1, -1
            idx = bisect.bisect_left(arr, val)
            if idx != len(arr):
                maxVal = arr[idx]
                if arr[idx] == val:
                    maxVal = arr[idx]
                    res.append([minVal, maxVal])
                    continue
            if idx != 0:
                minVal = arr[idx - 1]
            res.append([minVal, maxVal])
        return res
