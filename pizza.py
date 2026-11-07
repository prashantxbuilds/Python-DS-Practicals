
# Graph representation using Dictionary

graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 1, 'D': 5},
    'C': {'A': 2, 'B': 1, 'D': 8, 'E': 10},
    'D': {'B': 5, 'C': 8, 'E': 2},
    'E': {'C': 10, 'D': 2}
}

distance = {}
visited = []

start = 'A'

for node in graph:
    distance[node] = 999

distance[start] = 0

# Dijkstra's Algorithm

for i in range(len(graph)):

    min_dist = 999
    current = None

    for node in graph:
        if node not in visited and distance[node] < min_dist:
            min_dist = distance[node]
            current = node

    if current is None:
        break

    visited.append(current)

    for neighbour in graph[current]:
        new_dist = distance[current] + graph[current][neighbour]

        if new_dist < distance[neighbour]:
            distance[neighbour] = new_dist

# Display Minimum Delivery Time

print("Pizza Shop Location:", start)
print("\nMinimum Delivery Time:")

for node in distance:
    print("Location", node, "=", distance[node], "minutes")
