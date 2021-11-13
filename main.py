import unittest
import numpy as np
from alg import sort, numerics

class TestSortMethods(unittest.TestCase):
    def test_merge(self):

        for _ in range(10):
            a = np.random.randint(50000, size=50000) - 50000/2
            b = np.random.randint(50000, size=50000) - 50000/2
            np.sort(a)
            np.sort(b)
            merged = sort.merge(a,b)

            self.assertEqual(len(merged), len(a)+len(b))

            for i in range(1,len(merged)):
                sorted = True

                if (merged[i] < merged[i-1]):
                    sorted = False
                    break
        
        
class TestNumericsMethods(unittest.TestCase):
    def test_karatsuba(self):
        x = 1234561
        y = 9876541
        xy = numerics.karatsuba(x,y)
        self.assertEqual(xy,x*y)

        x2 = 1234567876543234
        y2 = 9237647912846106
        x2y2 = numerics.karatsuba(x2, y2)
        self.assertEqual(x2y2,x2*y2)

    def test_rec_mult(self):
        x = 1234561
        y = 9876541
        xy = numerics.rec_mult(x,y)
        self.assertEqual(xy,x*y)

        x2 = 1234567876543234
        y2 = 9237647912846106
        x2y2 = numerics.rec_mult(x2, y2)
        self.assertEqual(x2y2,x2*y2)


def main():
    print("Running algorithms")
    unittest.main()

if __name__ == "__main__":
    main()