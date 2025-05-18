from typing import List, Optional

from pycparser.ply.yacc import debug_file

from common.base import TreeNode


class Solution75:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]

    def sort_colors_insert(self, nums: List[int]) -> None:
        for i in range(1, len(nums)):
            for j in range(i, 0, -1):
                if nums[j] < nums[j - 1]:
                    nums[j], nums[j - 1] = nums[j - 1], nums[j]

    def sort_colors_merge(self, nums: List[int]) -> None:
        """
        使用归并排序
        """

        def merge_sort(nums: List[int], left: int, right: int) -> None:
            if left >= right:
                return
            mid = (left + right) // 2
            merge_sort(nums, left, mid)
            merge_sort(nums, mid + 1, right)
            merge(nums, left, mid, right)

        def merge(nums: List[int], left: int, mid: int, right: int) -> None:
            temp = []
            i, j = left, mid + 1
            while i <= mid and j <= right:
                if nums[i] < nums[j]:
                    temp.append(nums[i])
                    i += 1
                else:
                    temp.append(nums[j])
                    j += 1
            while j <= right:
                temp.append(nums[j])
                j += 1
            while i <= mid:
                temp.append(nums[i])
                i += 1
            start_idx = left
            for i in range(len(temp)):
                nums[start_idx] = temp[i]
                start_idx += 1

        merge_sort(nums, 0, len(nums) - 1)


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution1367:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        return self.dfs(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)

    def dfs(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if not head:
            return True
        if not root:
            return False
        if head.val != root.val:
            return False
        return self.dfs(head.next, root.left) or self.dfs(head.next, root.right)


class Solution109:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        nums = []

        def dfs(node: Optional[ListNode]):
            if not node:
                return
            nums.append(node.val)
            dfs(node.next)

        def build_tree(arr: List[int], l: int, r: int) -> Optional[TreeNode]:
            if l > r:
                return None
            mid = (l + r) // 2
            root = TreeNode(arr[mid])
            root.left = build_tree(arr, l, mid - 1)
            root.right = build_tree(arr, mid + 1, r)
            return root

        dfs(head)
        return build_tree(nums, 0, len(nums) - 1)


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution116:
    def connect(self, root: Optional[Node]) -> Optional[Node]:
        def travers(pre: Optional[Node], last: Optional[Node]):
            if not pre or not last:
                return
            pre.next = last
            travers(pre.left, pre.right)
            travers(pre.right, last.left)
            travers(last.left, last.right)

        if not root:
            return root
        travers(root.left, root.right)
        return root


class Solution117:
    def connect(self, root: 'Node') -> 'Node':
        q = [] if not root else [root]
        while q:
            sz = len(q)
            pre = q[0]
            for _ in range(sz):
                node = q.pop(0)
                if node != pre:
                    pre.next = node
                pre = node
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return root
