from typing import List, Optional


class Solution0107:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        tmp = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                tmp[j][len(matrix) - i - 1] = matrix[i][j]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j] = tmp[i][j]


class Solution0108:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        points = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    points.append((i, j))
        x = len(matrix)
        y = len(matrix[0])
        for i, j in points:
            for yz in range(y):
                matrix[i][yz] = 0
            for xz in range(x):
                matrix[xz][j] = 0


class Solution0109:
    def isFlipedString(self, s1: str, s2: str) -> bool:
        def isFlipedString(self, s1: str, s2: str) -> bool:
            return len(s1) == len(s2) and s2 in s1 + s1


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeDuplicateNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        int_set = set()
        dummy = ListNode(-1)
        cur = dummy
        while head:
            if head.val not in int_set:
                cur.next = head
                cur = cur.next
                int_set.add(head.val)
            head = head.next
        cur.next = None
        return dummy.next


class Solution0202:
    def kthToLast(self, head: Optional[ListNode], k: int) -> int:
        slow = head
        fast = head
        while k > 0:
            fast = fast.next
        while fast:
            slow = slow.next
            fast = fast.next
        return slow.val


class Solution0203:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next


class Solution0204:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy2 = ListNode(-1)

        cur = dummy
        cur2 = dummy2
        while head:
            if head.val < x:
                cur.next = head
                cur = cur.next
            else:
                cur2.next = head
                cur2 = cur2.next
            head = head.next
        cur.next = dummy2.next
        cur2.next = None
        return dummy.next


class Solution0205:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        carray = 0
        cur = dummy
        while l1 or l2 or carray:
            s = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carray
            carray, val = divmod(s, 10)
            cur.next = ListNode(val)
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next
