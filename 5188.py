from pprint import pprint


tc = int(input())
for test in range(tc):
    N =int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    ans = [[0]* N for _ in range(N)]
    ans[0][0] = arr[0][0]
    for i in range(1,N):
        ans[0][i] = ans[0][i-1] + arr[0][i]
        ans[i][0] = ans[i-1][0] + arr[i][0]
    
    for i in range(1,N):
        for j in range(1,N):
            ans[i][j] = arr[i][j] + min(ans[i-1][j], ans[i][j-1])
        for k in range(N):
            print(ans[k])
        print()

    print(f'#{test+1} {ans[N-1][N-1]}')

#1 2 3         1 3 6         1 3 6       1 3 6
#2 3 4   --->  3 0 0 ------> 3 6 10----> 3 6 10
#3 4 5         6 0 0         6 0 0       6 10 15

#dfs
""" def dfs(x,y,temp):
    global ans
    if temp > ans:
        return
    if x == y == N-1:
        if ans > temp:
            ans = temp
        return
    for i,j in [[0,1],[1,0]]:
        if x+i<N and y+j <N:
            dfs(x+i,y+j,temp+arr[x+i][y+j])

tc = int(input())
for test in range(tc):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    ans = 2* N * 10
    dfs(0,0,arr[0][0])
    print(f'#{test+1} {ans}')
 """