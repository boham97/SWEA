def dfs(x, y, dct, n):
    global cnt
    if visited[4][x][y] == 1 or cnt <= n + (2*N-x-y-2) or visited[dct][x][y] <= n:
        return
    if x == N and y == N + 1:
        if cnt > n:
            cnt = n
            for x,y,dc,n in temp:
                visited[dc][x][y] = n
        return
    visited[4][x][y] = 1
    temp.append([x,y,dct,n])
    if arr[x][y] == 0:
        visited[3][x][y] = 1
        visited[2][x][y] = 1
        visited[1][x][y] = 1
        visited[0][x][y] = 1
    elif arr[x][y] <3:
        if dct == 0:
            dfs(x, y+1, dct, n + 1)
        elif dct == 1:
            dfs(x + 1, y, dct, n + 1)
        elif dct == 2:
            dfs(x, y - 1, dct, n + 1)
        elif dct == 3:
            dfs(x - 1, y, dct, n + 1)
    elif arr[x][y] >2:
        if dct == 0:
            dfs(x + 1, y, 1, n + 1)
            dfs(x - 1, y, 3, n + 1)
        elif dct == 1:
            dfs(x, y + 1, 0, n + 1)
            dfs(x, y - 1, 2, n + 1)
        elif dct == 2:
            dfs(x + 1, y, 1, n + 1)
            dfs(x - 1, y, 3, n + 1)
        else:
            dfs(x, y + 1, 0, n + 1)
            dfs(x, y - 1, 2, n + 1)
    visited[4][x][y] = 0
    temp.pop()
    
    
tc = int(input())
for test in range(tc):
    N = int(input())
    cnt = N*N+2
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[[cnt] * (N + 2) for _ in range(N + 2)] for _ in range(4)]
    visited.append([[0]* (N+2) for _ in range(N+2)])
    arr.append([0] * (N + 2))
    arr.insert(0, [0] * (N + 2))
    for i in range(1, N + 1):
        arr[i].append(0)
        arr[i].insert(0, 0)
    arr[1][0] = 1
    arr[N][N + 1] = 1
    temp =[]
    dfs(1, 0, 0, 0)
    print(f'#{test + 1} {cnt-1}')

