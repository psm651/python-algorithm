import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())
miro = [sys.stdin.readline().rstrip() for _ in range(N)]
visited=[[0]*M for _ in range(N)]
queue=deque([])
dx=[-1,1,0,0]
dy=[0,0,1,-1]

queue.append([0,0])
visited[0][0] = 1
while queue:
    x, y = queue.popleft()
    if x == N-1 and y ==M-1:
        print(visited[x][y])
        break
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0<=nx<N and 0<=ny<M:
            if miro[nx][ny] == '1' and visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y]+1
                queue.append([nx,ny])