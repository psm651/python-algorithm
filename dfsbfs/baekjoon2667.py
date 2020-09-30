import sys
N = int(sys.stdin.readline())
M = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
stack = []


def DFS(depth, x, y):
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            if M[nx][ny] == '1' and not visited[nx][ny]:
                visited[nx][ny] = True
                depth = DFS(depth+1, nx, ny)
    return depth


for i in range(N):
    for j in range(N):
        if M[i][j] == '1' and not visited[i][j]:
            visited[i][j] = True
            stack.append(DFS(1, i, j))
stack.sort()
print(len(stack))
for i in range(len(stack)):
    print(stack[i])