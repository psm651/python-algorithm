# -*- coding: utf-8 -*- 
import sys
from collections import deque 

N, M = map(int,sys.stdin.readline().split())#M행N열
matrix = [sys.stdin.readline().split() for _ in range(M)]
visited=[[False] * N for _ in range(M)]
queue=deque([])
dx = [-1,1,0,0]
dy = [0,0,1,-1]

#초기값 세팅
for i in range(M):
    for j in range(N):
        if matrix[i][j] == '1':
            visited[i][j] = True
            queue.append((i,j))

def BFS():
    day=0
    while queue:
        qsize = len(queue)
        for i in range(qsize):
            x, y = queue.popleft()
            for j in range(4):
                nx, ny = x+dx[j], y+dy[j]
                if 0<= nx < M and 0<= ny < N:
                    if matrix[nx][ny]!='-1' and not visited[nx][ny]:
                        visited[nx][ny] = True
                        matrix[nx][ny] = '1'
                        queue.append([nx,ny])
        day += 1
    for i in range(M):
        for j in range(N):
            if matrix[i][j] == '0':
                return -1
    return day-1
print(BFS())