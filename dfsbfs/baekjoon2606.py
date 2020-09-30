import sys
n = int(sys.stdin.readline())#node
e = int(sys.stdin.readline())#edge

def DFS(graph, start):
    visited=[]
    stack=[start]
    edge = 0
    while stack:
        node = stack.pop()
        if node not in visited:
            edge += 1
            visited.append(node)
            stack.extend(graph[node])
    return visited



#그래프 생성
graph =[set([]) for _ in range(n+1)]
for _ in range(e):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].add(b)
    graph[b].add(a)

print(len(DFS(graph,1))-1)