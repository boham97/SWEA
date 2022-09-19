def f(n):
    global ans
    if n == 0:
        return
    else:
        f(son1[n])
        arr[n] = ans
        ans += 1
        f(son2[n])


tc = int(input())
for test in range(tc):
    N = int(input())
    son1 = [0] * (N+1)
    son2 = [0] * (N+1)
    arr = [0] *(N+1)

    for i in range(1,N//2 + 1):
        if 2*i < N+1:
            son1[i] = 2*i
        if 2*i+1 < N+1:
            son2[i] = 2*i +1
    ans = 1
    f(1)
    print(f'#{test+1} {arr[1]} {arr[N//2]}')