import itertools

tc = int(input())
for test in range(tc):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    team = list(itertools.combinations(range(N), N//2))
    nums = len(team)
    ans = 20000 * 8
    for t in range(nums//2):
        if ans == 0:
            break
        link = team[t]
        start = team[nums-t-1]
        temp = 0
        for i in link:
            for j in link:
                temp += arr[i][j]
        for i in start:
            for j in start:
                temp -= arr[i][j]
        if abs(temp) < ans:
            ans = abs(temp)

    print(f'#{test+1} {ans}')