import sys
sys.setrecursionlimit(50000)  # 재귀제한높이설정(기본값이상으로 안해주면 런타임에러) ※기본값:1000
T = int(sys.stdin.readline().rstrip())  # T 테스트케이스
for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())  # M 가로 N 세로 K 배추개수
    G = [[False]*N for _ in range(M)]
    visited = [[False]*N for _ in range(M)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]

    moim = 0
    for _ in range(K):
        x, y = map(int, sys.stdin.readline().split())
        G[x][y] = True

    def DFS(x, y):
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < M and 0 <= ny < N:
                if G[nx][ny] == True and not visited[nx][ny]:
                    visited[nx][ny] = True
                    DFS(nx, ny)

    for i in range(M):
        for j in range(N):
            if G[i][j] == True and not visited[i][j]:
                visited[i][j] = True
                moim += 1
                DFS(i, j)
    print(moim)