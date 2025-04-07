from functools import cache
from typing import List, Optional

from common.base import TreeNode

# 416 等和子集
class Solution416:
    def canPartition(self, nums: List[int]) -> bool:
        @cache
        def dfs(i:int,j:int)->bool:
            if i >= len(nums):
                return j == 0
            if j == 0:
                return True
            return (j >= nums[i] and dfs(i+1,j-nums[i])) or dfs(i+1,j)
        
        sum_v :int = sum(nums)
        if sum_v % 2 == 1:
            return False
        half:int = sum_v / 2
        return dfs(0,half)
    
    def can_partition(self,nums:List[int]):
        sum_v :int = sum(nums)
        if sum_v % 2 == 1:
            return False
        half:int = sum_v / 2
        m :int = len(nums)
        dp :[[bool]] = [[False for _ in range(half+1)] for _ in range(m+1)]# type: ignore
        for i in range(len(dp)):
            dp[i][0] = True
        for i in range(1,m+1):
            for j in range(1,half+1):
                if j >= nums[i-1]:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[m][half]

# 652 寻找重复的子树
class Solution652:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        tree_cnt :dict[str,int] = {}
        res:List[TreeNode] = []
        def travers(node:TreeNode)->str:
            if not node:
                return "#"
            left:str = travers(node.left)
            right :str= travers(node.right)
            sub :str= left +","+right+","+str(node.val)
            tree_cnt[sub]+=1
            if tree_cnt[sub] == 2:
                res.append(node)
            return sub
        travers(root)
        return res

        