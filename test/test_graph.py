import unittest
import logging
import networkx as nx
from alg import graph
import matplotlib.pyplot as plt

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

    WEIGHTED2 = nx.Graph()
    WEIGHTED2.add_edge(7, 6, weight = 1)
    WEIGHTED2.add_edge(8, 2, weight = 2)
    WEIGHTED2.add_edge(6, 5, weight = 2)
    WEIGHTED2.add_edge(0, 1, weight = 4)
    WEIGHTED2.add_edge(2, 5, weight = 4)
    WEIGHTED2.add_edge(8, 6, weight = 6)
    WEIGHTED2.add_edge(2, 3, weight = 7)
    WEIGHTED2.add_edge(7, 8, weight = 7)
    WEIGHTED2.add_edge(0, 7, weight = 8)
    WEIGHTED2.add_edge(1, 2, weight = 8)
    WEIGHTED2.add_edge(3, 4, weight = 9)
    WEIGHTED2.add_edge(5, 4, weight = 10)
    WEIGHTED2.add_edge(1, 7, weight = 11)
    WEIGHTED2.add_edge(3, 5, weight = 14)

    WEIGHTED3 = nx.Graph()
    WEIGHTED3.add_edge(0, 1, weight = 10)
    WEIGHTED3.add_edge(0, 2, weight = 6)
    WEIGHTED3.add_edge(0, 3, weight = 5)
    WEIGHTED3.add_edge(1, 3, weight = 15)
    WEIGHTED3.add_edge(2, 3, weight = 4)   

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

    def test_kruskal(self):
        mst1, mst1_val = graph.kruskal(sample_graphs.WEIGHTED1)
        self.assertEqual(mst1_val, 14)

        mst1_set = set(mst1)
        should_eq = set([('a','b'), ('a', 'd'), ('b', 'e'), 
                        ('e','c'), ('c','f')])

        self.assertEqual(mst1_set, should_eq)

        mst2, mst2_val = graph.kruskal(sample_graphs.WEIGHTED2)
        self.assertEqual(mst2_val, 37)

        mst2_set = set(mst2)

        should_eq2 = set([
            (0, 1), (2, 1), (7, 6),
            (6, 5), (2, 5), (8, 2),
            (2, 3), (3, 4)
        ])
        self.assertEqual(mst2_set, should_eq2)

        mst3, mst3_val = graph.kruskal(sample_graphs.WEIGHTED3)
        self.assertEqual(mst3_val, 19)

        mst3_set = set(mst3)
        self.assertEqual(mst3_set, set([(2,3), (0,3), (0,1)]))    

    def test_prim(self):
        mst1, mst1_val = graph.prim(sample_graphs.WEIGHTED1)
        
        self.assertEqual(mst1_val, 14)

        mst2, mst2_val = graph.prim(sample_graphs.WEIGHTED2)
        self.assertEqual(mst2_val, 37)

        mst3, mst3_val = graph.prim(sample_graphs.WEIGHTED3)
        self.assertEqual(mst3_val, 19)  

    def test_dfs(self):

        # Create Disconnected graph partions are {1,2,3,4} {5,7,8,9}
        g = nx.Graph()
        g.add_edge(1, 2)
        g.add_edge(2,3)
        g.add_edge(1,4)
        g.add_edge(5,7)
        g.add_edge(8,9)
        g.add_edge(5,9)

        self.assertNotEqual(graph.dfs(g, 1, 4), None)
        self.assertEqual(graph.dfs(g, 1, 8), None)
        self.assertEqual(graph.dfs(g,2,2), [2])
        
        with self.assertRaises(Exception):
            graph.dfs(g,19,1)

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

    def test_find(self):
        dj = graph.DisjointSet([0, 1, 2, 3, 4])

        # Simulate merging 0 and 1
        dj.set_map[1] = 0

        # Simulate merging 3 and 2
        dj.set_map[3] = 2

        self.assertEqual(dj.find(0), 0)
        self.assertEqual(dj.find(1), 0)
        self.assertEqual(dj.find(2), 2)
        self.assertEqual(dj.find(3), 2)
        self.assertEqual(dj.find(4), 4)

        # Simulate merging 4 and 3
        root_4 = dj.set_map[4] # root of 4 is 4
        root_3 = dj.set_map[3] # root of 3 is 2
        dj.set_map[4] = 2

        self.assertEqual(dj.find(0), 0)
        self.assertEqual(dj.find(1), 0)
        self.assertEqual(dj.find(2), 2)
        self.assertEqual(dj.find(3), 2)
        self.assertEqual(dj.find(4), 2)

    def test_union(self):
        dj = graph.DisjointSet(['a', 'b', 'c', 'd', 'z'])

        dj.union('a', 'd')
        shouldEQ = {'a': 'd', 'b': 'b', 'c': 'c', 'd': 'd', 'z': 'z'}
        self.assertEqual(dj.set_map, shouldEQ)

        dj.union('c', 'b')
        shouldEQ = {'a': 'd', 'b': 'b', 'c': 'b', 'd': 'd', 'z': 'z'}
        self.assertEqual(dj.set_map, shouldEQ)

        dj.union('z', 'a')
        shouldEQ = {'a': 'd', 'b': 'b', 'c': 'b', 'd': 'd', 'z': 'd'}
        self.assertEqual(dj.set_map, shouldEQ)

        dj.union('c', 'z')
        shouldEQ = {'a': 'd', 'b': 'd', 'c': 'b', 'd': 'd', 'z': 'd'}
        self.assertEqual(dj.set_map, shouldEQ)

if __name__ == '__main__':
    unittest.main()
    