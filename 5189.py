def check(starting, temp, num):
    global ans
    if temp > ans:
        return
    elif num ==N-1:
        temp += cost[starting][0]
        if temp < ans:
            ans = temp
        return
    else:
        for i in range(N):
            if visited[i] == 0:
                visited[i] = 1
                check(i, temp + cost[starting][i], num+1)
                visited[i] = 0
tc = int(input())
for test in range(tc):
    N = int(input())
    cost = [list(map(int,input().split())) for _ in range(N)]
    visited = [0] * N
    visited[0] = 1
    ans = 99999999
    check(0,0,0)
    print(f'#{test+1} {ans}')