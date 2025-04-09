import unittest

from april.chart0409 import Solution3375


class TestSolution3375(unittest.TestCase):
    def setUp(self):
        self.solution = Solution3375()

    def test_minOperations_EmptyList_ReturnsNegativeOne(self):
        result = self.solution.minOperations([], 5)
        self.assertEqual(result, -1)

    def test_minOperations_AllElementsLessThanK_ReturnsNegativeOne(self):
        result = self.solution.minOperations([1, 2, 3], 5)
        self.assertEqual(result, -1)

    def test_minOperations_FirstElementEqualsK_ReturnsLengthMinusOne(self):
        result = self.solution.minOperations([5, 5, 6, 7], 5)
        self.assertEqual(result, 2)

    def test_minOperations_FirstElementGreaterThanK_ReturnsLength(self):
        result = self.solution.minOperations([6, 7, 8], 5)
        self.assertEqual(result, 3)

    def test_minOperations_MixedElements_ReturnsCorrectValue(self):
        result = self.solution.minOperations([1, 2, 3, 5, 6, 7], 5)
        self.assertEqual(result, -1)


if __name__ == '__main__':
    unittest.main()
