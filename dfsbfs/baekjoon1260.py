from collections import deque
import sys
n, m, v = map(int, sys.stdin.readline().split())

def DFS(graph, start):
    visited = []
    stack = [start]
    
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack += sorted(graph[node], reverse=True)
    return visited

def BFS(graph, start):
    visited = []
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            queue += sorted(graph[node])
    return visited

graph = [set([])for _ in range(n+1)]
for _ in range(m):
    a, b = map(int,sys.stdin.readline().split())
    graph[a].add(b)
    graph[b].add(a)

print(*DFS(graph, v))
print(*BFS(graph, v))