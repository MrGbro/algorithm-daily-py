from collections import Counter
from unittest import TestCase

from may.chart0530 import Solution0104, Solution0105


class TestSolution0104(TestCase):
    def test_can_permute_palindrome(self):
        inst = Solution0104()
        inst.canPermutePalindrome("code")
        s = Counter("abcd")
        s2 = Counter("abdf")
        s3 = s - s2
        print(s3)


class TestSolution0105(TestCase):
    def test_one_edit_away(self):
        inst = Solution0105()
        res = inst.oneEditAway("ab","bc")
        self.assertTrue(res,"测试失败")

