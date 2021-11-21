import unittest
from alg import parallel
import numpy as np
from datetime import datetime

class TestParallelMethods(unittest.TestCase):
    # def test_Parallel_Sum(self):
    #     nums = np.random.randint(0,1000, 50)
    #     self.assertEqual(parallel.Sum(nums), sum(nums))

        # nums = np.random.randint(-1 * (10 ** 3), 10 ** 3, 10 ** 3)
        # self.assertEqual(parallel.Sum(nums), sum(nums))

        # nums = np.random.randint(-1 * (10 ** 3), 10 ** 3, 10 ** 3)
        # self.assertEqual(parallel.Sum(nums), sum(nums))

        # nums = np.random.randint(-1 * (10 ** 6), 10 ** 6, 10 ** 6)
        # self.assertEqual(parallel.Sum(nums), sum(nums))

    def test_PoolSum(self):

        # Correctness Test

        nums = np.random.randint(-1000, 1000, 1000)
        self.assertEqual(parallel.PoolSum(nums), sum(nums))


        # Beter Performance Test
        # nums = np.random.randint(0,1000, 10 ** 9)

        # start1 = datetime.now()
        # normal_sum = sum(nums)
        # end1 = datetime.now()
        # duration1 = end1 - start1

        # start2 = datetime.now()
        # pool_sum = parallel.PoolSum(nums)
        # end2 = datetime.now()
        # duration2 = end2 - start2
        
        # self.assertEqual(parallel.PoolSum(nums), np.sum(nums))
        # self.assertLessEqual(duration2, duration1)