import unittest

from may.chart0517 import Solution75


class Solution75Test(unittest.TestCase):
    def test_sortColors(self):
        s = Solution75()
        nums = [2, 0, 2, 1, 1, 0]
        s.sortColors(nums)
        self.assertEqual(nums, [0, 0, 1, 1, 2, 2])
        nums = [2, 0, 1]
        s.sortColors(nums)
        self.assertEqual(nums, [0, 1, 2])
        nums = [0]
        s.sortColors(nums)

    def test_sort_colors_merge(self):
        s = Solution75()
        nums = [2, 0, 2, 1, 1, 0]
        s.sort_colors_merge(nums)
        self.assertEqual(nums, [0, 0, 1, 1, 2, 2])
        nums = [2, 0, 1]
        s.sortColors(nums)
        self.assertEqual(nums, [0, 1, 2])
        nums = [0]
        s.sortColors(nums)
