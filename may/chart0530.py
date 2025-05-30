from typing import List, Counter


class Solution1577:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        dict1 = {}
        dict2 = {}
        for v in nums1:
            dict1[v] = dict1.get(v,0)+1
        for v in nums2:
            dict2[v] = dict2.get(v,0)+1

        def cnt_func(arr:List[int],arr2:List[int],cnt_map:dict[int,int])->int:
            cnt = 0
            for v in arr:
                s = v ** 2
                for j in arr2:
                    if s % j != 0:
                        continue
                    else:
                        t = s // j
                        if t == j:
                            c = cnt_map.get(t,0)
                            cnt += 0 if c <= 1 else c * (c-1) // 2
                        else:
                            c1 = cnt_map.get(j,0)
                            c2 = cnt_map.get(t,0)
                            cnt += c1 * c2
            return cnt
        return cnt_func(nums1,nums2,dict2) + cnt_func(nums2,nums1,dict1)


class Solution0102:
    def isUnique(self, astr: str) -> bool:
        record = set()
        for i in astr:
            if i in record:
               return False
            record.add(i)
        return True


class Solution0103:
    def replaceSpaces(self, S: str, length: int) -> str:
        s = S[:length]
        return s.replace(" ","%20")


class Solution0104:
    def canPermutePalindrome(self, s: str) -> bool:
        cnt = Counter(s)
        odd_cnt = 0
        for k,v in cnt.items():
            if v % 2 == 1:
                odd_cnt += 1
        n = len(s)
        if n % 2 ==0:
            return odd_cnt == 0
        else:
            return odd_cnt == 1


class Solution0105:
    def oneEditAway(self, first: str, second: str) -> bool:
        if first == second:
            return True
        if abs(len(first)-len(second)) > 1:
            return False
        l1 = 0
        l2 = 0
        delta = 0
        while l1 < len(first) and l2 < len(second):
            if first[l1] != second[l2]:
                delta += 1
                if len(first)  == len(second):
                    l1 += 1
                    l2 += 1
                if len(first) > len(second):
                    l1 += 1
                if len(first) < len(second):
                    l2 += 1
            else:
                l1 += 1
                l2 += 1
        delta += (len(first)-l1) + (len(second)-l2)
        return delta == 1


class Solution0106:
    def compressString(self, S: str) -> str:
        cur = 0
        pre = ""
        res = ""
        for v in S:
            if pre == "" or pre == v:
                cur += 1
            else:
                res += pre+str(cur)
                cur = 1
                pre = v
        res += pre+str(cur)
        return res







