def dfs(depth, length):
    global ans
    if depth >= ans:
        return
    if valid():
        ans = depth
        return
    else:
        for i in range(length, D):
            for j in range(W):
                arr[i][j] = 0
            dfs(depth+1, i+1)
            for j in range(W):
                arr[i][j] = 1
            dfs(depth+1, i+1)
            for j in range(W):
                arr[i][j] = arr2[i][j]


def valid():
    logic = 0
    for i in range(W):
        temp = 1
        for j in range(D-1):
            if arr[j][i] == arr[j+1][i]:
                temp += 1
            else:
                temp = 1
            if temp == K:
                logic += 1
                break
        else:
            break

    if logic == W:
        return 1
    else:
     return 0


tc = int(input())
for test in range(tc):
    D, W, K = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(D)]
    arr2 = [arr[i][:] for i in range(D)]
    ans = K
    temp2 = [0] *  W
    dfs(0,0)
    print(f'#{test+1} {ans}')
