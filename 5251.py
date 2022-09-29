tc = int(input())
for test in range(tc):
    N, E = map(int,input().split())
    graph = [[10**12]*(N+1) for _ in range(N+1)]
    for i in range(E):
        x,y,e = map(int,input().split())
        graph[x][y] = e
    for i in range(N+1):
        graph[i][i] = 0
    d = graph[0][:]
    used = {0}
    while len(used) != N:
        temp = 10 ** 12
        next = 0
        for i in range(N+1):
            if i not in used and d[i]< temp:
                temp = d[i]
                next = i
        used.add(next)
        for i in range(N+1):
            d[i] = min(d[i], d[next]+graph[next][i])
    print(f'#{test+1} {d[-1]}')