import heapq
import networkx as nx
from sys import maxsize

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

def prim(graph: nx.Graph):

    # Begin prim's algorithm from some arbitrary node in the graph
    start_node = list(graph.nodes())[0]

    # Initialize the min weight to add to MST for each node to be infinity
    min_weights = {node: maxsize for node in graph.nodes()}

    # Since no min edge to add is found, set min_edge_from[node] to be None for all nodes
    min_edge_from = {node: None for node in graph.nodes()}

    # List to store edges in the final Min spanning tree
    mst = []

    # Store the total weight for the MST
    mst_val = 0

    # Priority queue which stores the next cheapest node to visit
    queue = []

    # Stores the nodes who have already been visited
    visited = set()

    # Enqueue the start node with a weight of 0
    heapq.heappush(queue, (0, start_node))

    # While the queue isn't empty
    while len(queue) > 0:
        # Pop the top element of the queue
        _ , node1 = heapq.heappop(queue)

        # For the first node, there's no actual edge, so don't add to MST
        if not node1 == start_node:

            # Append the min edge between node1 and the others in the MST
            mst += [(min_edge_from[node1], node1)]

            # Add the weight of the edge being added to the weight for the MST
            edge_weight = graph.get_edge_data(min_edge_from[node1], node1)['weight']
            log.debug(f'Edge: {(min_edge_from[node1], node1)}: {edge_weight}')
            mst_val += edge_weight

        # Add Node 1 to the set of visited nodes
        visited.add(node1)

        # Iterate over the neighbors of node 1
        for node2 in graph.neighbors(node1):

            # Lookup the weight of the edge between node1 and the current neighbor
            edge_weight = graph.get_edge_data(node1, node2)['weight']

            if edge_weight < min_weights[node2] and not node2 in visited:
                min_weights[node2] = edge_weight
                min_edge_from[node2] = node1

                # Update value in prioity queue

                # Lookup the idx of node2 if it exists in the queue, otherwise idx = None
                idx_in_queue = next((idx for idx, pair in enumerate(queue) if pair[1] == node2), None)

                if not idx_in_queue == None:
                    # Update the edge_weight for the item in the queue
                    queue[idx_in_queue] = (edge_weight, node2)

                    # Need to heapify to maintain heap structure
                    heapq.heapify(queue)

                else:
                    # Enqueue node2 with the weight from node1 to node2 since it's not in q yet
                    heapq.heappush(queue, (edge_weight, node2))
    
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
