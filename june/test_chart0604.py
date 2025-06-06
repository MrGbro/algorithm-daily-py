from unittest import TestCase

from june.chart0604 import Solution0503


class TestSolution(TestCase):
    def test_reverse_bits(self):
        inst = Solution0503()
        inst.reverseBits(-1)
