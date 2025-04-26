from typing import Optional, List

from common.base import ListNode


# LeetCode 725
class Solution725:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        nodes: List[ListNode] = []
        while head:
            nodes.append(head)
            head = head.next

        sz: int = len(nodes)
        rest = sz % k
        cnt = sz // k
        idx = 0
        start = 0
        j = 0
        result: List[Optional[ListNode]] = [None] * k
        while idx < sz:
            result[start] = nodes[idx]
            start += 1
            if j < rest:
                idx = idx + cnt + 1
                j += 1
            else:
                idx = idx + cnt
            if idx <= sz - 1:
                nodes[idx - 1].next = None
        return result


node = ListNode(1, ListNode(2, ListNode(3)))
solution = Solution725()
ls = solution.splitListToParts(node, 5)
