What is the state representation?
A: The state representation is a tuple using row and column that marks the agent's current position on the grid.
Why does BFS guarantee the shortest path in this grid?
A: BFS guarantees the shortest path as it explorers the grid layer by layer which expands all nodes at distance d before
any node at d+1.
Since each move is 1 step, the first contact with G will be the guaranteed fewest steps which results in shortest path.
My results:

Path length = 8
Nodes expanded = 15