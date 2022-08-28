def dfs(month, money):
    global min_pay
    if month >= 12:
        if min_pay > money:
            min_pay = money
        return
    else:
        for i in range(3):
            if i ==0:
                dfs(month+1, min(money + pay[1],money + pay[0]*plan[month]))
            elif i ==1:
                dfs(month+3, money + pay[2])
            elif i ==2:
                dfs(month+12, money + pay[3])



tc = int(input())

for test in range(tc):
    pay = list(map(int,input().split()))
    plan = list(map(int,input().split()))
    min_pay = pay[3]

    dfs(0,0)
    print(f'#{test+1} {min_pay}')
