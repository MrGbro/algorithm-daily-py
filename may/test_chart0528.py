from unittest import TestCase

from may.chart0528 import Solution658


class TestSolution658(TestCase):
    def test_find_closest_elements(self):
        inst = Solution658()
        inst.findClosestElements([1,1,1,10,10,10],1,9)
