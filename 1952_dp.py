tc = int(input())
for test in range(tc):
    price = list(map(int,input().split()))
    plan = list(map(int,input().split()))
    pay = [3000* 32] *13
    pay[0] = 0
    pay[12] = price[3]
    for i in range(12):
        pay[i+1] = min(pay[i+1], pay[i]+min(price[0]*plan[i], price[1]))
        if i+3 < 13:
            pay[i+3] = min(pay[i+3], pay[i]+price[2])
        else:
            pay[12] = min(pay[12], pay[i]+price[2])
    print(f'#{test+1} {pay[12]}')
