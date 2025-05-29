from unittest import TestCase

from may.chart0522 import Solution1234, Solution632


class TestSolution1234(TestCase):
    def test_balanced_string(self):
        inst = Solution1234()
        v = inst.balancedString("QWER")
        self.assertEqual(v, 0)
        v2 = inst.balancedString("QQWR")
        self.assertEqual(v2, 1)


class TestSolution632(TestCase):
    def test_smallest_range(self):
        inst = Solution632()
        res = inst.smallestRange([[4,10,15,24,26],[0,9,12,20],[5,18,22,30]])
        print(res)
