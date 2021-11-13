import heapq

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
