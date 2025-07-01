from common.base import ListNode, list_node_of, Node


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        tmp = []
        while head:
            tmp.append(head)
            head = head.next
        n = len(tmp)
        half = (n + 1) // 2
        pre_half = tmp[:half]
        suf_half = tmp[half:]
        real_suf = suf_half[::-1]

        ls = []
        i, j = 0, 0
        while i < len(pre_half) and j < len(real_suf):
            ls.append(pre_half[i])
            ls.append(real_suf[j])
            i += 1
            j += 1
        while i < len(pre_half):
            ls.append(pre_half[i])
            i += 1
        while j < len(real_suf):
            ls.append(real_suf[j])
            j += 1
        for i,v in enumerate(ls):
            if i<n-1:
                v.next = ls[i+1]
            else:
                v.next = None

inst = Solution()
inst.reorderList(list_node_of([1,2,3,4]))


class SolutionLCR029:
    def flatten(self, head: 'Node') -> 'Node':
        def dfs(node:'Node')->'Node':
            if not node:
                return node
            cur = node
            last = None
            while cur:
                nxt = cur.next
                if cur.child:
                    last_child = dfs(cur.child)
                    nxt = cur.next
                    cur.next = cur.child
                    cur.child.prev = cur
                    if nxt:
                        last_child.next = nxt
                        nxt.prev = last_child
                    cur.child = None
                    last = last_child
                else:
                    last = cur
                cur = nxt
            return last
        dfs(head)
        return head

class SolutionLCR029:
    def insert(self, head: "Node", insertVal: int) -> "Node":
        node = Node(insertVal)
        if not head:
            node.next = node
            return node
        if head.next == head:
            head.next = node
            node.next = head
            return head
        slow = head
        fast = head.next
        while fast:
            if slow.val <= insertVal <= fast.val:
                break
            if slow.val > fast.val:
                if insertVal > slow.val or insertVal < fast.val:
                    break
            slow = slow.next
            fast = fast.next
        slow.next = node
        node.next = fast
        return head



