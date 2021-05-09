from alg import sort
import unittest
import numpy as np

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
        
                self.assertTrue(sorted)

def main():
    unittest.main()
    print("Running algorithms")

if __name__ == "__main__":
    main()
