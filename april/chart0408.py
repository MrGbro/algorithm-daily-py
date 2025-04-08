from traceback import format_tb
from typing import List, Optional

from common.base import TreeNode


# 3396 使数组互不相同的最少操作次数
class Solution3396:
    def minimumOperations(self, nums: List[int]) -> int:
        tmp: [int] = [0] * 101
        cnt_map: [int, int] = {}
        for num in nums:
            tmp[num] += 1
            if tmp[num] >= 2:
                cnt_map[num] = tmp[num]

        res: int = 0
        if len(cnt_map) > 0:
            for i in range(0, len(nums), 3):
                for gen in range(i, i + 3 if i + 3 < len(nums) else len(nums)):
                    v = nums[gen]
                    if v in cnt_map:
                        cnt_map[v] -= 1
                        if cnt_map[v] == 1:
                            del cnt_map[v]
                res += 1
                if len(cnt_map) == 0:
                    break
        return res


class MergeSort:
    def sort(self, nums: List[int]):
        tmp: List[int] = [0] * len(nums)

        def merge(ls: List[int], left: int, mid: int, right: int):
            for i in range(left, right + 1):
                tmp[i] = ls[i]
            i: int = left
            j: int = mid + 1
            k: int = left
            while i <= mid and j <= right:
                if tmp[i] <= tmp[j]:
                    ls[k] = tmp[i]
                    i += 1
                else:
                    ls[k] = tmp[j]
                    j += 1
                k += 1
            while i <= mid:
                ls[k] = tmp[i]
                i += 1
                k += 1
            while j <= right:
                ls[k] = tmp[j]
                j += 1
                k += 1

        def sort(ls: List[int], left: int, right: int):
            if left >= right:
                return
            mid: int = (left + right) // 2
            sort(ls, left, mid)
            sort(ls, mid + 1, right)
            merge(ls, left, mid, right)

        if len(nums) < 2:
            return
        sort(nums, 0, len(nums) - 1)


# 230 节
class Solution230:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cnt: int = 0
        res: int = 0
        def inorder(node: Optional[TreeNode], limit: int):
            nonlocal cnt,res
            if node is None:
                return
            inorder(node.left, limit)
            cnt = cnt + 1
            if cnt == limit:
                res = node.val
                return
            inorder(node.right, limit)
        inorder(root, k)
        return res
