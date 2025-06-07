# Definition for singly-linked list.
import math
from collections import deque
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution0206:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        tmp = []
        while head:
            tmp.append(head.val)
            head = head.next
        l, r = 0, len(tmp) - 1
        while l < r:
            if tmp[l] != tmp[r]:
                return False
            l += 1
            r -= 1
        return True


class Solution0207:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        l1 = headA
        l2 = headB
        while l1 != l2:
            l1 = l1.next if l1 else headB
            l2 = l2.next if l2 else headA
        return l1


class Solution0208:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
            if slow == fast:
                ans = head
                while ans != slow:
                    ans = ans.next
                    slow = slow.next
                return ans
        return None


class TripleInOne0301:

    def __init__(self, stackSize: int):
        self.stack_size = stackSize
        self.array = [0] * (stackSize * 3)
        self.start_point = [0, 0, 0]

    def push(self, stackNum: int, value: int) -> None:
        idx = self.start_point[stackNum]
        if idx >= self.stack_size:
            return
        self.array[idx + stackNum * self.stack_size] = value
        self.start_point[stackNum] += 1

    def pop(self, stackNum: int) -> int:
        idx = self.start_point[stackNum]
        if idx <= 0:
            return -1
        res = self.array[idx + stackNum * self.stack_size - 1]
        self.start_point[stackNum] -= 1
        return res

    def peek(self, stackNum: int) -> int:
        idx = self.start_point[stackNum]
        if idx <= 0:
            return -1
        res = self.array[idx + stackNum * self.stack_size - 1]
        return res

    def isEmpty(self, stackNum: int) -> bool:
        idx = self.start_point[stackNum]
        return idx <= 0


inst = TripleInOne0301(1)
inst.push(0, 1)
inst.push(0, 2)
inst.pop(0)
inst.pop(0)
inst.pop(0)
res = inst.isEmpty(0)
print(res)


class MinStack0302:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = [math.inf]

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.min_stack.append(min(x, self.min_stack[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


class StackOfPlates0303:

    def __init__(self, cap: int):
        self.cap = cap
        self.stk = []

    def push(self, val: int) -> None:
        if self.cap == 0:
            return
        if not self.stk or len(self.stk[-1]) >= self.cap:
            self.stk.append([])
        self.stk[-1].append(val)

    def pop(self) -> int:
        return self.popAt(len(self.stk) - 1)

    def popAt(self, index: int) -> int:
        ans = -1
        if 0 <= index < len(self.stk):
            ans = self.stk[index].pop()
            if not self.stk[index]:
                self.stk.pop(index)
        return ans


class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.s2.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self.s1:
            if self.s2:
                while self.s2:
                    self.s1.append(self.s2.pop())
        return self.s1.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.s1:
            return self.s1[-1]
        return self.s2[0]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.s1 and not self.s2


s = MyQueue()
s.push(1)
s.push(2)
print(s.peek())
print(s.pop())
print(s.empty())


class SortedStack:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, val: int) -> None:
        if not self.s1:
            self.s1.append(val)
        else:
            while self.s1 and val > self.s1[-1]:
                self.s2.append(self.s1.pop())
            self.s1.append(val)
            while self.s2:
                self.s1.append(self.s2.pop())

    def pop(self) -> None:
        if self.isEmpty():
            return
        self.s1.pop()

    def peek(self) -> int:
        if self.isEmpty():
            return -1
        return self.s1[-1]

    def isEmpty(self) -> bool:
        return len(self.s1) == 0


class AnimalShelf:

    def __init__(self):
        self.q = [deque(), deque()]

    def enqueue(self, animal: List[int]) -> None:
        i, j = animal
        self.q[j].append(i)

    def dequeueAny(self) -> List[int]:
        if not self.q[0] or (self.q[1] and self.q[1][0] < self.q[0][0]):
            return self.dequeueDog()
        return self.dequeueCat()

    def dequeueDog(self) -> List[int]:
        return [-1, -1] if not self.q[1] else [self.q[1].popleft(), 1]

    def dequeueCat(self) -> List[int]:
        return [-1, -1] if not self.q[0] else [self.q[0].popleft(), 0]
