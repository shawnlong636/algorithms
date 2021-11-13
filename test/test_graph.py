import unittest
import logging
from alg import graph

class TestGraphMethods(unittest.TestCase):
    
    def test_flood_fill(self):
        table1 = [
            [1, 0],
            [0, 0]
        ]

        start = (0,0)
        new_val = 0
        ff1 = graph.flood_fill(table1, start, new_val)

        shouldEQ1 = [
            [0, 0],
            [0, 0]
        ]

        self.assertEqual(ff1, shouldEQ1)

        start = (1,1)
        new_val = 7

        ff1 = graph.flood_fill(table1, start, new_val)

        shouldEQ1 = [
            [7, 7],
            [7, 7]
        ]

        self.assertEqual(ff1, shouldEQ1)

        table2 = [
            [1, 1, 1, 0, 1, 2, 2],
            [0, 0, 0, 0, 2, 2, 1],
            [3, 3, 0, 2, 3, 4, 4]
        ]

        start = (0,3)
        new_val = 2
        ff2 = graph.flood_fill(table2, start, new_val)

        shouldEQ2 = [
            [1, 1, 1, 2, 1, 2, 2],
            [2, 2, 2, 2, 2, 2, 1],
            [3, 3, 2, 2, 3, 4 ,4]
        ]

        self.assertEqual(ff2, shouldEQ2)

        start = (2,5)
        new_val = 0
        ff2 = graph.flood_fill(table2, start, new_val)

        shouldEQ2 = [
            [1, 1, 1, 2, 1, 2, 2],
            [2, 2, 2, 2, 2, 2, 1],
            [3, 3, 2, 2, 3, 0, 0]
        ]

        self.assertEqual(ff2, shouldEQ2)

        with self.assertRaises(Exception):
            ff2(table2, (9,999), -1,)

if __name__ == '__main__':
    unittest.main()