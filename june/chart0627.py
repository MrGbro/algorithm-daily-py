from common.base import ListNode


class Solution019:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l <= r:
            if s[l] != s[r]:
                break
            l += 1
            r -= 1
        if l > r:
            return True
        if l == 0:
            s1 = s[1:]
            s2 = s[:r]
            return s1 == s1[::-1] or s2 == s2[::-1]
        else:
            s1 = s[:l] + s[l+1:]
            s2 = s[:r] + s[r+1:]
            return s1 == s1[::-1] or s2 == s2[::-1]

# inst = Solution019()
# res = inst.validPalindrome("abbac")
# print(res)


class Solution020:
    def countSubstrings(self, s: str) -> int:
        def is_palindromic(i:int,j:int)->bool:
            ans = 0
            if i < 0 or j >= len(s):
                return False
            while i >= 0 and j < len(s):
                if s[i] != s[j]:
                    break
                ans += 1
                i -= 1
                j += 1
            return ans
        cnt = 0
        for i in range(len(s)):
            cnt += is_palindromic(i,i)
            cnt += is_palindromic(i,i+1)
        return cnt
inst = Solution020()
res = inst.countSubstrings("aaa")
print(res)


class Solution021:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = head
        fast = dummy
        slow = dummy
        for _ in range(n):
            fast = fast.next
        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dummy.next


class Solution022:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow = head
        fast = head
        while True:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None


