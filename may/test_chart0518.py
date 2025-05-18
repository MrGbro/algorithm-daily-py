from unittest import TestCase

from may.chart0518 import Solution634


class TestSolution634(TestCase):
    def test_find_max_average(self):
        inst = Solution634()
        result: float = inst.findMaxAverage([-1], 1)
        self.assertEqual(result, -1.0, "compute error")
