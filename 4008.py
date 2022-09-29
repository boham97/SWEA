def dfs(last,n):
    global mx, mn
    if n == N:
        if last > mx:
            mx = last
        if last < mn:
            mn = last
        return
    else:
        for i in range(4):
            if arr[i] >0:
                arr[i] -= 1
                if i == 0:
                    dfs(last+num[n],n+1)
                if i == 1:
                    dfs(last-num[n],n+1)
                if i == 2:
                    dfs(last*num[n],n+1)
                if i == 3:
                    if last< 0:
                        last = (-1*last)//num[n]
                        last *= -1
                        dfs(last,n+1)
                    else:
                        dfs(last//num[n],n+1)
                arr[i] += 1


tc = int(input())
for test in range(tc):
    N = int(input())
    arr = list(map(int,input().split()))
    num = list(map(int, input().split()))
    mx = -1 * 10 ** 8
    mn = 10**8
    dfs(num[0],1)
    print(f'{test+1} {mx-mn}')