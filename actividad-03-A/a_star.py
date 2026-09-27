import heapq

def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(start, goal, neighbors, cost=1):
    """
    start, goal: tuplas (fila, col)
    neighbors(pos) -> lista de posiciones válidas
    """
    open_heap = []
    heapq.heappush(open_heap, (manhattan(start, goal), 0, start))
    g_score = {start: 0}
    came_from = {}

    while open_heap:
        f, g, current = heapq.heappop(open_heap)

        if current == goal:
            path = [current]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            return list(reversed(path))

        for nxt in neighbors(current):
            new_g = g_score[current] + cost
            if nxt not in g_score or new_g < g_score[nxt]:
                g_score[nxt] = new_g
                came_from[nxt] = current
                h = manhattan(nxt, goal)
                heapq.heappush(open_heap, (new_g + h, new_g, nxt))

    return None

# Cuadrícula 3x3 sin obstáculos de prueba
def grid_neighbors(pos):
    r, c = pos
    moves = []
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            moves.append((nr, nc))
    return moves

if __name__ == "__main__":
    camino = astar((0, 0), (2, 2), grid_neighbors)
    print("A* (0,0) → (2,2):", camino)