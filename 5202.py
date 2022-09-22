tc = int(input())
for test in range(tc):
    N = int(input())
    work = [[0]*2 for _ in range(N)]
    for i in range(N):
        strt, nd = map(int,input().split())
        work[i][0], work[i][1] = nd, strt
    work.sort()
    ans = 0
    time = 0
    for i in range(N):
        if time <= work[i][1]:
            ans +=1 
            time = work[i][0]
    print(f'#{test+1} {ans}')