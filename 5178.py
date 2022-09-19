tc = int(input())
for test in range(tc):
    N, M, L = map(int,input().split())
    arr = [0] * (N+1)
    for i in range(M):
        node, num = map(int,input().split())
        arr[node] = num
    for i in range(N,0, -1):
        arr[i//2] += arr[i]
        print(i//2, i, arr[i//2])
    print(f'#{test+1} {arr[L]}')