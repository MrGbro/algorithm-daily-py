from unittest import TestCase

from june.chart0611 import Solution1621, Solution1626


class TestSolution1621(TestCase):
    def test_find_swap_values(self):
        inst = Solution1621()
        inst.findSwapValues([4, 1, 2, 1, 1, 2], [3, 6, 3, 3])


class TestSolution1626(TestCase):
    def test_calculate(self):
        inst = Solution1626()
        # res = inst.calculate(" 3+5 / 2 ")
        # self.assertEqual(5,res,"计算错误")
        res = inst.calculate("1*2-3/4+5*6-7*8+9/10")
        self.assertEqual(1, res, "计算错误")
