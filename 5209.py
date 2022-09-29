def dfs(i,temp):
    global ans
    if temp > ans:        
        return
    elif i == N and temp < ans:
        ans = temp
        return
    else:
        for j in range(i,N):
            arr[i], arr[j] = arr[j], arr[i]
            dfs(i+1, temp - max_graph[i] + graph[i][arr[i]])
            arr[i], arr[j] = arr[j], arr[i]

tc = int(input())
for test in range(tc):
    N = int(input())
    graph = [list(map(int,input().split())) for _ in range(N)]
    arr =list(range(N))
    ans = 99*N
    max_graph = [0] * N
    max_rate = 0
    for i in range(N):
        max_graph[i] = min(graph[i])
        max_rate += (max_graph[i])
    dfs(0,max_rate)
    print(f'#{test+1} {ans}')
