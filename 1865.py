def dfs(i,temp):
    global ans
    if temp < ans:          #남은 일꾼들의 최대 확율의 합이 ans보다 작으면 stop
        return
    elif i == N and temp > ans:
        ans = temp
        return
    else:
        for j in range(i,N):
            arr[i], arr[j] = arr[j], arr[i]
            if graph[i][arr[i]] == 0:
                arr[i], arr[j] = arr[j], arr[i]
                continue
            dfs(i+1, temp / max_graph[i] * graph[i][arr[i]]/100)
            arr[i], arr[j] = arr[j], arr[i]

tc = int(input())
for test in range(tc):
    N = int(input())
    graph = [list(map(int,input().split())) for _ in range(N)]
    arr =list(range(N))
    ans = 0
    max_graph = [0] * N
    max_rate = 1
    for i in range(N):
        max_graph[i] = max(graph[i])/100
        max_rate *= (max_graph[i])
    dfs(0,max_rate)
    print(f'#{test+1} {ans*100:.6f}')
