import unittest
from alg import parallel
import numpy as np

class TestParallelMethods(unittest.TestCase):
    def test_par_sum(self):
        nums = np.random.randint(0,1000, 50)

        self.assertEqual(parallel.Sum(nums), sum(nums))