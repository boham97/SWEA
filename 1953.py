from collections import deque
dx = [0, -1, 1, 0]
dy = [-1, 0, 0, 1]
able = [
    [0,0,0,0],
    [1,1,1,1],
    [0,1,1,0],
    [1,0,0,1],
    [0,1,0,1],
    [0,0,1,1],
    [1,0,1,0],
    [1,1,0,0],
]

tc = int(input())
for test in range(tc):
    N, M, R, C,L = map(int, input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    visited = [[0]*M for _ in range(N)]
    deq = deque()
    deq.append((R,C))
    visited[R][C] = 1
    while deq:
        x, y = deq.popleft()
        for i in range(4):
            if 0 <= x+dx[i] < N and 0 <= y+dy[i] < M and able[arr[x][y]][i] and able[arr[x+dx[i]][y+dy[i]]][3-i] and visited[x+dx[i]][y+dy[i]] == 0:
                if visited[x][y] < L:
                    deq.append((x+dx[i],y+dy[i]))
                    visited[x+dx[i]][y+dy[i]] = visited[x][y] + 1
    ans = 0
    for i in range(N):
        for j in range(M):
            if visited[i][j] != 0:
                ans += 1
    print(f'#{test+1} {ans}')
    
