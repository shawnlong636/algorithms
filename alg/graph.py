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

class DisjointSet:
	set_map = {}

	def __init__(self, nodes: [int] = []):
		self.set_map = {node: node for node in nodes}

	def from_graph(self, graph: nx.Graph):
		self.set_map = {node: node for node in graph.nodes()}

	def find(self, node1, node2) -> bool:
		if not node1 in self.set_map:
			raise ValueError(f'Node: {node1} not in set')

		if not node2 in self.set_map:
			raise ValueError(f'Node: {node2} not in set')

		if self.set_map.get(node1) == self.set_map.get(node2):
			return True

		else:
			return False

	def union(self, node1: int, node2: int):
		if not self.find(node1, node2):
			self.set_map[node2] = self.set_map[node1]

	def __str__(self):
		return str(self.set_map)
