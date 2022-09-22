tc = int(input())
for test in range(tc):
    N,M = map(int,input().split())
    n = list(map(int,input().split()))
    m = list(map(int,input().split()))
    n.sort()
    m.sort()
    ans = 0
    while n and m:
        if n[-1] <= m[-1]:
            ans += n[-1]
            n.pop()
            m.pop()
        else:
            n.pop()
    print(f'#{test+1} {ans}')