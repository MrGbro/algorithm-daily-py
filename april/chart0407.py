from functools import cache
from typing import List, Optional

from common.base import TreeNode


# 416 等和子集
class Solution416:
    def canPartition(self, nums: List[int]) -> bool:
        @cache
        def dfs(i: int, j: int) -> bool:
            if i >= len(nums):
                return j == 0
            if j == 0:
                return True
            return (j >= nums[i] and dfs(i + 1, j - nums[i])) or dfs(i + 1, j)

        sum_v: int = sum(nums)
        if sum_v % 2 == 1:
            return False
        half: int = sum_v / 2
        return dfs(0, half)

    def can_partition(self, nums: List[int]):
        sum_v: int = sum(nums)
        if sum_v % 2 == 1:
            return False
        half: int = sum_v / 2
        m: int = len(nums)
        dp: [[bool]] = [[False for _ in range(half + 1)] for _ in range(m + 1)]  # type: ignore
        for i in range(len(dp)):
            dp[i][0] = True
        for i in range(1, m + 1):
            for j in range(1, half + 1):
                if j >= nums[i - 1]:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[m][half]


# 652 寻找重复的子树
class Solution652:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        tree_cnt: dict[str, int] = {}
        res: List[TreeNode] = []

        def travers(node: TreeNode) -> str:
            if not node:
                return "#"
            left: str = travers(node.left)
            right: str = travers(node.right)
            sub: str = left + "," + right + "," + str(node.val)
            if sub not in tree_cnt:
                tree_cnt[sub] = 0
            tree_cnt[sub] += 1
            if tree_cnt[sub] == 2:
                res.append(node)
            return sub

        travers(root)
        return res

class MergeSort:
    def merge_sort(self, nums: List[int]) -> List[int]:
        def merge(left: List[int], right: List[int]) -> List[int]:
            res: List[int] = []
            i: int = 0
            j: int = 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    res.append(left[i])
                    i += 1
                else:
                    res.append(right[j])
                    j += 1
            res.extend(left[i:])
            res.extend(right[j:])
            return res
        if len(nums) <= 1:
            return nums
        mid: int = len(nums) // 2
        lt: List[int] = self.merge_sort(nums[:mid])
        rt: List[int] = self.merge_sort(nums[mid:])
        return merge(lt, rt)

sort_util = MergeSort()
print(sort_util.merge_sort([5, 2, 3, 1]))

# 202 快乐数
class Solution202:
    def isHappy(self, n: int) -> bool:
        def get_next(n: int) -> int:
            total_sum: int = 0
            while n > 0:
                n, digit = divmod(n, 10)
                total_sum += digit ** 2
            return total_sum
        while n != 1 and n != 4:
            n = get_next(n)
        return n == 1
