import unittest
import logging
import networkx as nx
from alg import graph

class sample_graphs:

    WEIGHTED1 = nx.Graph()
    WEIGHTED1.add_edge('a', 'b', weight = 1)
    WEIGHTED1.add_edge('a', 'e', weight = 3)
    WEIGHTED1.add_edge('a', 'd', weight = 4)
    WEIGHTED1.add_edge('b', 'e', weight = 2)
    WEIGHTED1.add_edge('b', 'd', weight = 4)
    WEIGHTED1.add_edge('d', 'e', weight = 4)
    WEIGHTED1.add_edge('e', 'c', weight = 4)
    WEIGHTED1.add_edge('e', 'f', weight = 7)
    WEIGHTED1.add_edge('c', 'f', weight = 3)

    adj_list = [
        "0 1 4 5",
        "1 0 2 6",
        "2 1 3 7",
        "3 2 4 6",
        "4 0 3 5 8 9",
        "5 0 4 7",
        "6 1 8 9",
        "7 2 5 9",
        "8 3 4 6",
        "9 4 6 7"
    ]

    UNWEIGHTED1 = nx.parse_adjlist(adj_list, nodetype = int)

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

class TestDisjointSet(unittest.TestCase):

    def test_constructor(self):
        dj1 = graph.DisjointSet()
        self.assertEqual(dj1.set_map, {})

        dj2 = graph.DisjointSet([])
        self.assertEqual(dj2.set_map, {})

        dj3 = graph.DisjointSet([0, 0, 0, 0])
        self.assertEqual(dj3.set_map, {0: 0})

        dj4 = graph.DisjointSet([0, 1, 2, 4])
        self.assertEqual(dj4.set_map, {0: 0, 1: 1, 2: 2, 4: 4})

    def test_from_graph(self):
        dj = graph.DisjointSet(sample_graphs.WEIGHTED1)

        self.assertEqual(dj.set_map, {node: node for node in sample_graphs.WEIGHTED1.nodes()})

        dj = graph.DisjointSet(sample_graphs.UNWEIGHTED1)

        self.assertEqual(dj.set_map, {node: node for node in sample_graphs.UNWEIGHTED1.nodes()})

if __name__ == '__main__':
    unittest.main()
    