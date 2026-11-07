
# Graph using Adjacency Matrix for DFS

vertices = ['A', 'B', 'C', 'D', 'E']

matrix = [
    [0, 1, 1, 0, 0],
    [1, 0, 0, 1, 1],
    [1, 0, 0, 0, 1],
    [0, 1, 0, 0, 0],
    [0, 1, 1, 0, 0]
]

# Graph using Adjacency List for BFS

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'E'],
    'D': ['B'],
    'E': ['B', 'C']
}

# DFS using Adjacency Matrix

visited = []
stack = ['A']

while stack:
    node = stack.pop()

    if node not in visited:
        visited.append(node)

        index = vertices.index(node)

        for i in range(len(vertices) - 1, -1, -1):
            if matrix[index][i] == 1:
                if vertices[i] not in visited:
                    stack.append(vertices[i])

print("DFS Traversal:", visited)

# BFS using Adjacency List

visited = []
queue = ['A']

while queue:
    node = queue.pop(0)

    if node not in visited:
        visited.append(node)

        for neighbour in graph[node]:
            if neighbour not in visited and neighbour not in queue:
                queue.append(neighbour)

print("BFS Traversal:", visited)
