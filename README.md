# Exercise 1: Path Availability in a Directed Graph (DFS)

This exercise implements a simple directed graph using custom `Vertex`, `Edge`, and `Graph` classes. The goal is to determine whether there is a path between two vertices using Depth-First Search (DFS).

## 🔍 Functionality

The `path_availability()` method checks if there's a path from a given start vertex (`label_x`) to a destination vertex (`label_y`). It performs the following steps:

- Identifies the start and destination vertices based on their labels.
- If either vertex is not found, it returns `False`.
- Uses recursive Depth-First Search (DFS) to explore possible paths.
- Keeps track of visited vertices to avoid cycles and unnecessary repetitions.
- Returns `True` if a path exists, otherwise `False`.

## 📌 Key Concepts

- **Directed Graph**: The graph edges have direction; traversal only follows the direction of edges.
- **DFS Traversal**: The algorithm explores as deep as possible along each branch before backtracking.
- **Visited Set**: A set is used to keep track of already visited vertices to prevent infinite loops.

## 💡 Example Use Case

This could be applied in a navigation system where intersections are vertices and one-way roads are edges. The function helps determine if a route exists from one point to another following the road directions.

## 🧠 Summary

This exercise reinforces understanding of graphs, DFS, recursion, and how to manage visited states while traversing through a directed graph structure.
