delx = [-1,-1,-1,0,0,1,1,1]
dely = [-1, 0, 1, -1, 1,-1,0,1]

tc = int(input())
for test in range(tc):
    N,M = map(int, input().split())
    mat = [[0] * N for _ in range(N)]
    mat[N//2][N//2] = 2
    mat[N//2][N//2-1] = 1
    mat[N//2-1][N//2] = 1
    mat[N//2-1][N//2-1] = 2

    for turn in range(M):
        y, x, color = map(int, input().split())
        y -= 1
        x -= 1
        mat[x][y] = color
        for i in range(8):
            flag = 0
            dx = x+delx[i]
            dy = y + dely[i]
            while 0 <= dx < N and 0 <= dy < N and mat[dx][dy] and mat[dx][dy] == 3 - color:
                dx = dx + delx[i]
                dy = dy + dely[i]
                flag = 1
            if flag and 0 <= dx < N and 0 <= dy < N and mat[dx][dy] == color:
                while dx != x or dy != y:
                    mat[dx][dy] = color
                    dx = dx - delx[i]
                    dy = dy - dely[i]
    two = one = 0
    for i in range(N):
        for j in range(N):
            if mat[i][j] == 2:
                two += 1
            elif mat[i][j] ==1:
                one += 1
    print(f'#{test+1} {one} {two}')
