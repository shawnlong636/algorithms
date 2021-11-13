import unittest
from alg import numerics

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

    if __name__ == '__main__':
        unittest.main()