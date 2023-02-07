from cmath import inf
from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def bfs(self, start, end):
        queue = [start]
        visited = {start: 0}
        while queue:
            node = queue.pop(0)
            if node == end:
                return visited[end]
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    visited[neighbor] = visited[node] + 1
                    queue.append(neighbor)
        return float(-inf)

graph = Graph()

for i in range(int(input())):
    u, a, *v = map(int, input().split())
    for j in v:
        graph.add_edge(u, j)


start, end = input().split()
distance = graph.bfs(int(start), int(end))
print("Forevis alonis..." if distance < 0 else distance-1)

