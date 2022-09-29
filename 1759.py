def dij():
    while len(used) != N:
        temp = 10 ** 12
        next = 0
        for i in range(N+1):
            if i not in used and d[i]< temp:
                temp = d[i]
                next = i
        used.add(next)
        for i in range(1,N+1):
            d[i] = min(d[i], d[next]+graph[next][i])

tc = int(input())
for test in range(tc):
    N,M,X = map(int,input().split())
    graph = [[10**12]*(N+1) for _ in range(N+1)]
    for i in range(M):
        x,y,e = map(int,input().split())
        graph[x][y] = e
    for i in range(N+1):
        graph[i][i] = 0
    d = graph[X][:]
    used = {X}
    dij()
    temp = d[:]
    used = {X}
    graph = list(map(list, zip(*graph)))
    d = graph[X][:]
    dij()
    ans = 0
    for i in range(1,N+1):
        if d[i] +temp[i] > ans:
            ans = d[i] + temp[i]

    print(f'#{test+1} {ans}')