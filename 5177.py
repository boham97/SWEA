def heap_sort(x):
    if gab[x//2] > gab[x]:
        gab[x], gab[x//2] = gab[x//2], gab[x]
        heap_sort(x//2)

tc = int(input())
for test in range(tc):
    N = int(input())
    son1 = [0] * (N+1)
    son2 = [0] * (N+1)
    arr = list(map(int, input().split()))
    arr.insert(0,0)
    gab = [0] * (N+1)
    for i in range(1,N//2 + 1):
        if 2*i < N+1:
            son1[i] = 2*i
        if 2*i+1 < N+1:
            son2[i] = 2*i +1
    gab[1] = arr[1]
    for i in range(2,N+1):
        gab[i] = arr[i]
        heap_sort(i)
    ans = 0
    N = N//2
    while N:
        ans += gab[N]
        N = N//2
    print(f'#{test+1} {ans}')