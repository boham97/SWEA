tc = int(input())
for test in range(tc):
    arr = list(map(int,input().split()))
    cnt = [200] * (arr[0]+1)
    cnt[1] = 0
    N =arr[0]
    for i in range(1,N):
        for j in range(arr[i]+1):
            if i+j < N+1 and cnt[i+j] > cnt[i] +1:
                cnt[i+j] = cnt[i] +1
    print(f'#{test+1} {cnt[-1]-1}')
