def f(N):
    global ans
    if N == 0:
        return
    else:
        ans += 1
        f(son1[N])
        f(son2[N])


tc = int(input())
for test in range(tc):
    E, N = map(int,input().split())
    son1 = [0] * (E+2)
    son2 = [0] * (E+2)
    arr = list(map(int,input().split()))
    for i in range(E):
        if son1[arr[2*i]] == 0:
            son1[arr[2*i]] = arr[2*i+1]
        else:
            son2[arr[2*i]] = arr[2*i+1]

    ans = 0
    f(N)
    print(f'#{test+1} {ans}')