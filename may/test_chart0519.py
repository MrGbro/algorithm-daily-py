from unittest import TestCase

from may.chart0519 import Solution1423


class TestSolution1423(TestCase):
    def test_max_score(self):
        inst = Solution1423()
        res = inst.maxScore([1,2,3,4,5,6,1],3)
        self.assertEqual(res,12)
