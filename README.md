# 8puzzle_Astar_algorithm
This project solves the 8 puzzle problem using an A* algorithm

The 8 puzzle is a sliding puzzle with 9 grids in a 3x3 shape. The grid has 8 tiles that can slide in 4 directions (up, down, left, right). The goal is to shuffle the tiles into the correct order using the 8 sliding tiles and the single open space. The algorithm that I have used to solve this problem is the A* algorithm.

A* algorithm is an informed search or a best-first search that uses a heuristic function to evaluate a node in a path and stores all nodes in a list, sorted by the value of the heuristic function (the cost).
The path cost for a specific node n is calculated by combining two factors: the cost of the path from the start node to the node n (notated as g(n)), and an estimated cost (using a heuristic function) from the node to the goal (notated as h(n)).

Therefore the path cost is calculated using:
f(n) = g(n) + h(n)
