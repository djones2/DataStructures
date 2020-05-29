import unittest
import random
from sorts import *

class TestLab4(unittest.TestCase):

    def test_simple(self):
        random.seed(10)
        nums = random.sample(range(100), 10)
        nums2 = random.sample(range(100), 10)
        cmp1 = selection_sort(nums)
        cmp2 = insertion_sort(nums2)
        self.assertEqual(cmp1, 45)
        self.assertEqual(cmp2, 31)
        self.assertEqual(nums, [1, 4, 26, 35, 54, 59, 61, 62, 73, 83])
        self.assertEqual(nums2, [4, 5, 9, 20, 31, 41, 46, 62, 66, 95])

if __name__ == '__main__': 
    unittest.main()
