from unittest import TestCase

from may.chart0527 import Solution125


class TestSolution125(TestCase):
    def test_is_palindrome(self):
        inst = Solution125()
        inst.isPalindrome("A man, a plan, a canal: Panama")

