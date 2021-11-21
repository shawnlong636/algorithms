import unittest
from alg import parallel
import numpy as np

class TestParallelMethods(unittest.TestCase):
    def test_tiny_sum(self):
        nums = np.random.randint(0,1000, 50)
        self.assertEqual(parallel.Sum(nums), sum(nums))

    def test_small_sum(self):
        nums = np.random.randint(-1 * (10 ** 3), 10 ** 3, 10 ** 3)
        self.assertEqual(parallel.Sum(nums), sum(nums))

    def test_med_sum(self):
        nums = np.random.randint(-1 * (10 ** 3), 10 ** 3, 10 ** 3)
        self.assertEqual(parallel.Sum(nums), sum(nums))

    def test_big_sum(self):
        nums = np.random.randint(-1 * (10 ** 6), 10 ** 6, 10 ** 6)
        self.assertEqual(parallel.Sum(nums), sum(nums))
