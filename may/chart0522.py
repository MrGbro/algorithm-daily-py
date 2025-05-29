from collections import Counter
from math import inf
from typing import List


class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        one_cnt = s.count('1')
        if one_cnt < k:
            return ""
        l = 0
        one_count = 0
        min_left = []
        min_len = len(s)
        for i, v in enumerate(s):
            if v == '1':
                one_count += 1
            while one_count == k:
                length = i - l + 1
                if length < min_len:
                    min_len = length
                    while len(min_left) > 0:
                        min_left.pop(-1)
                    min_left.append(l)
                if length == min_len:
                    min_left.append(l)
                d = s[l]
                if d == '1':
                    one_count -= 1
                l += 1
        start = min_left[0]
        res = s[start:start + min_len]
        for i, v in enumerate(min_left):
            if i == 0:
                continue
            tmp = s[v:v + min_len]
            if tmp < res:
                res = tmp
        return res


class Solution1234:
    def balancedString(self, s: str) -> int:
        n = len(s)
        if n % 4 != 0:
            return 0
        cnt = n // 4
        cnt_map = Counter(s)
        need = {}
        for k, v in cnt_map.items():
            if v > cnt:
                need_cnt = v - cnt
                need[k] = need_cnt
        if len(need) == 0:
            return 0
        min_len = n
        l = 0
        window = {}
        valid = 0
        for i, v in enumerate(s):
            window[v] = window.get(v, 0) + 1
            if need.get(v, 0) != 0 and window[v] == need[v]:
                valid += 1
            while valid == len(need):
                min_len = min(min_len, i - l + 1)
                d = s[l]
                window[d] = window[d] - 1
                if need.get(d, 0) != 0 and need[d] > window[d]:
                    valid -= 1
                l += 1
        return min_len


class Solution2875:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        rem = target % total
        s, l = 0, 0
        ans = inf
        n = len(nums)
        for right in range(n * 2):
            s += nums[right % n]
            while s > rem:
                s -= nums[l % n]
                l += 1
            if s == rem:
                ans = min(ans, right - l + 1)
        return ans + target // total * n if ans < inf else -1


class Solution76:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        valid, l = 0, 0
        window = {}
        n = len(s)
        start = 0
        min_len = n+1
        for r, v in enumerate(s):
            window[v] = window.get(v,0)+1
            if need.get(v,0)>0 and need[v] == window[v]:
                valid += 1
            while valid == len(need):
                if min_len > r - l + 1:
                    min_len = r - l + 1
                    start = l
                d = s[l]
                if window[d] == need.get(d,0):
                    valid -= 1
                window[d] = window[d]-1
                l+=1

        return "" if min_len == n+1 else s[start:start+min_len]


class Solution632:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        n = len(nums)
        new_list = []
        for i,v in enumerate(nums):
            for j in v:
                new_list.append((j,i))
        new_list.sort(key=lambda item:item[0])
        l,delta = 0,0
        min_len = n+1
        window = {}
        res = []
        for i in range(len(new_list)):
            v,idx = new_list[i]
            window[idx] = window.get(idx,0)+1
            while len(window) == n:
                if min_len > i-l+1:
                    min_len = i-l+1
                    t = new_list[l + min_len - 1][0] - new_list[l][0]
                    if len(res) ==0:
                        res = [new_list[l][0], new_list[l + min_len - 1][0]]
                        delta = t
                    else:
                        res = res if delta < t else [new_list[l][0], new_list[l + min_len - 1][0]]
                d,dx = new_list[l]
                window[dx]-=1
                if window[dx] == 0:
                    del window[dx]
        return res




