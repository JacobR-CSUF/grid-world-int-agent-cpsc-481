# Jacob Rodas , CPSC 481-14, February 17th, 2026.
from collections import deque

# Grid definition
GRID = [
    ['S', '.', '.', '.', '.'],
    ['#', '#', '.', '#', '.'],
    ['.', '.', '.', '#', '.'],
    ['.', '#', '#', '#', '.'],
    ['.', '.', '.', '.', 'G']
]

def print_grid(grid):
    for row in grid:
        print(' '.join(row))
    print()

def find_position(grid, symbol):
    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if cell == symbol:
                return (r, c)
    return None

def get_neighbors(grid, pos):
    r, c = pos
    rows = len(grid)
    cols = len(grid[0])
    neighbors = []
    for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
        nr, nc = r+dr, c+dc
        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != '#':
            neighbors.append((nr, nc))
    return neighbors

def bfs(grid):
    start = find_position(grid, 'S')
    goal = find_position(grid, 'G')

    frontier = deque([start])
    visited = {start}
    parent = {start: None}
    nodes_expanded = 0

    while frontier:
        current = frontier.popleft()
        nodes_expanded += 1

        if current == goal:
            # Reconstruct path
            path = []
            node = current
            while node is not None:
                path.append(node)
                node = parent[node]
            path.reverse()
            return path, nodes_expanded

        for neighbor in get_neighbors(grid, current):
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                frontier.append(neighbor)

    return None, nodes_expanded

def main():
    print("Original grid:")
    print_grid(GRID)

    path, nodes_expanded = bfs(GRID)

    if path is None:
        print("No path found.")
        return

    print("Solved!")
    print(f"Path length (steps): {len(path) - 1}")
    print(f"Nodes expanded: {nodes_expanded}")
    print()

    # Mark path on grid copy
    result = [row[:] for row in GRID]
    for (r, c) in path:
        if result[r][c] not in ('S', 'G'):
            result[r][c] = '*'

    print("Grid with path (*):")
    print_grid(result)

if __name__ == "__main__":
    main()