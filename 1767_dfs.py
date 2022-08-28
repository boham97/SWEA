def dfs(num_core, cores, lens):
    global max_core, max_len
    if num_core == len(core):
        if cores > max_core:
            max_core = cores
            max_len = lens
        elif cores == max_core and max_len > lens:
            max_len = lens
        return
    for i in range(5):
        cnt = 0
        x, y =core[num_core][0], core[num_core][1]
        while i != 4 and 0<= x+dx[i] < N and 0 <= y+dy[i] < N:
            x = x+dx[i]
            y = y+dy[i]
            if arr[x][y] != 0:
                break
            cnt += 1
        else:
            if i != 4:
                x, y =core[num_core][0], core[num_core][1]
                while 0<= x+dx[i] < N and 0 <= y+dy[i] < N:
                    x = x+dx[i]
                    y = y+dy[i]
                    arr[x][y] = 2
                dfs(num_core + 1, cores+1, lens+cnt)
                x, y =core[num_core][0], core[num_core][1]
                while 0<= x+dx[i] < N and 0 <= y+dy[i] < N:
                    x = x+dx[i]
                    y = y+dy[i]
                    arr[x][y] = 0
            else:
                dfs(num_core +1, cores, lens)


dx = [-1, 1, 0, 0]
dy = [0 ,0 ,1, -1]

tc = int(input())
for test in range(tc):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    core = []
    max_core = 0
    max_len = 0

    for i in range(1,N-1):
        for j in range(1,N-1):
            if arr[i][j] == 1:
                core.append([i,j])
    dfs(0, 0, 0)
    print(f'#{test+1} {max_len}')