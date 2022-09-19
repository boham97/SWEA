arr = [[0] * 140 for _ in range(140)]
arr[0][0] = 1
arr[0][1] = 1
for i in range(139):
    for j in range(139):
        if arr[i][j] ==0:
            break
        else:
            arr[i+1][j] += arr[i][j]
            arr[i+1][j+1] += arr[i][j]

tc = int(input())

for test in range(tc):
    n,a,b = map(int,input().split())
    print(f'#{test+1} {arr[n-1][min(a,b)]}')
