def bfs(n,h):
    global ans
    if h > B or n == N:
        if B <= h < ans:
            ans = h
        return
    else:
        bfs(n+1, h)
        bfs(n+1,h+arr[n])


tc = int(input())
for test in range(tc):
    N, B = map(int,input().split())
    arr = list(map(int, input().split()))
    ans = 10000 * N
    bfs(0, 0)
    print(f'#{test+1} {ans}')