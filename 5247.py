tc = int(input())
for test in range(tc):
    N, M = map(int,input().split())
    que = [0] * 10**6
    visited = [0] * (1+10**6)
    que[0] = N
    top = 0
    bot = 0
    visited[N] = 1
    while top >= bot:
        now = que[bot]
        bot += 1
        temp = now +1
        if 0 < temp <=10**6 and visited[temp]== 0:
            top += 1
            que[top] = temp
            visited[temp] = visited[now] +1
            if temp == M:
                break
        temp = now -1
        if 0 <temp <=10**6 and visited[temp] == 0:
            top += 1
            que[top] = temp
            visited[temp] = visited[now] +1
            if temp == M:
                break
        temp = now *2
        if 0<temp <=10**6 and visited[temp] == 0:
            top += 1
            que[top] = temp
            visited[temp] = visited[now] +1
            if temp == M:
                break
        temp = now -10
        if 0<temp <=10**6 and visited[temp] == 0:
            top += 1
            que[top] = temp
            visited[temp] = visited[now] +1
            if temp == M:
                break
    print(f'#{test+1} {visited[M]-1}')
