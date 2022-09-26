dx = [0,-1,1,0,0]
dy = [0,0,0,-1,1]
tc = int(input())
for test in range(tc):
    N, M, K = map(int,input().split())
    arr =[list(map(int,input().split())) for _ in range(K)]
    while M:
        for k in range(K):
            if arr[k][2] != 0:
                arr[k][0] += dx[arr[k][3]]
                arr[k][1] += dy[arr[k][3]]
                if arr[k][0] == 0 or arr[k][0] == N-1 or arr[k][1] == 0 or arr[k][1] == N-1:
                    arr[k][2] = arr[k][2]//2
                    if arr[k][3]%2 == 1:
                        arr[k][3] += 1
                    else:
                        arr[k][3] -= 1
        for k in range(K):
            if arr[k][2] == 0:
                continue
            temp = [[],[]]
            for j in range(k,K):
                if arr[k][0] == arr[j][0] and arr[k][1] == arr[j][1]:
                    temp[0].append(arr[j][3])
                    temp[1].append(arr[j][2])
                    arr[j][2] = 0
            arr[k][2] = sum(temp[1])
            arr[k][3] = temp[0][temp[1].index(max(temp[1]))]
        M -= 1

    ans = 0
    for i in range(K):
        ans += arr[i][2]
    print(f'#{test+1} {ans}')