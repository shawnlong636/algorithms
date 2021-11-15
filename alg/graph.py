import heapq
import networkx as nx

def flood_fill(table2D: [[int]], start_idx: (int, int) = (0,0), new_val: int = 9):

    def get_neighbors(table2D: [[int]], idx: (int, int)) -> [int]:
        row_length = len(table2D)
        col_length = len(table2D[0])

        neighbors = []

        row, col = idx

        if row - 1 >= 0: neighbors += [(row - 1, col)]
        if row + 1 < row_length: neighbors += [(row + 1, col)]
        if col - 1 >= 0: neighbors += [(row, col - 1)]
        if col + 1 < col_length: neighbors += [(row, col + 1)]

        return neighbors
    target_val = table2D[start_idx[0]][start_idx[1]]

    visited = set()
    queue = []

    heapq.heappush(queue, start_idx)

    while len(queue) > 0:
        cur_idx = heapq.heappop(queue)
        row, col = cur_idx
        table2D[row][col] = new_val
        visited.add(cur_idx)

        neighbors = get_neighbors(table2D, cur_idx)

        for neighbor in neighbors:
            row,col = neighbor
            if not neighbor in visited and table2D[row][col] == target_val:
                heapq.heappush(queue, neighbor)


    return table2D

def kruskal(graph: nx.graph):
    mst = []
    mst_val = 0

    dj = DisjointSet()
    dj.from_graph(graph)

    edges = [(attr_dict['weight'], (x, y)) for x, y, attr_dict in graph.edges(data=True)]
    edges = sorted(edges)

    for weight, edge in edges:
        x, y = edge

        if not dj.find(x) == dj.find(y):
            mst.append(edge)
            mst_val += weight
            dj.union(x,y)

    return (mst, mst_val)

class DisjointSet:
    set_map = {}

    def __init__(self, nodes = []):
	    self.set_map = {node: node for node in nodes}

    def from_graph(self, graph: nx.Graph):
	    self.set_map = {node: node for node in graph.nodes()}

    def find(self, node):
        if self.set_map.get(node) == node:
            return node
        else:
            return self.find(self.set_map[node])

    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)
        self.set_map[root1] = root2

    def __str__(self):
	    return str(self.set_map)
