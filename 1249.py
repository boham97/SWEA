from collections import deque

dx = [-1,1,0,0]
dy = [0,0,1,-1]
def bfs():
    while que:
        i,j = que.popleft()
        for k in range(4):
            delx, dely = i+dx[k], j + dy[k]
            if 0 <= delx < N and 0 <= dely < N:
                if visited[delx][dely] > visited[i][j]+graph[delx][dely]:
                    visited[delx][dely] = visited[i][j]+graph[delx][dely]
                    que.append([delx,dely])

tc = int(input())
for test in range(tc):
    N = int(input())
    graph = [list(map(int,input())) for _ in range(N)]
    visited = [[1000000]*N for _ in range(N)]
    visited[0][0] = 0
    que = deque()
    que.append([0,0])

    bfs()
    print(f'#{test+1} {visited[N-1][N-1]}')