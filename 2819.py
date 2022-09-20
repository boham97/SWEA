delta = [[1,0],[-1,0],[0,1],[0,-1]]
def dfs(x,y,hab,n):
    if n == 7:
        ans.append(hab)
        return
    else:

        for i in range(4):
            dx = x + delta[i][0]
            dy = y + delta[i][1]
            if 0<= dx < 4 and 0 <= dy < 4 :
                dfs(dx,dy,hab*10 + matrix[x][y], n+1)

tc = int(input())
for test in range(tc):
    matrix = [list(map(int, input().split())) for _ in range(4)]
    ans = []
    for i in range(4):
        for j in range(4):
            dfs(i,j,0,0)
    print(f'#{test+1} {len(set(ans))}')

    #모든 경우를 저장한후 set()으로 겹치는것을 줄이는게 시간이 적게 걸린다