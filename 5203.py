def babygin(arr,player):
    i = 0
    while i < 10:
        if arr[i] > 2:
            return player
        elif i+2 < 10:
            if arr[i]*arr[i+1]*arr[i+2] != 0:
                return player
        i += 1
    return 0

tc = int(input())
for test in range(tc):
    temp = list(map(int,input().split()))
    cnt1 = [0] * 10
    cnt2 = [0] * 10
    for i in range(len(temp)):
        if i%2 == 0:
            cnt1[temp[i]] += 1
            logic = babygin(cnt1,1)
            if logic:
                break
        else:
            cnt2[temp[i]] += 1
            logic = babygin(cnt2,2)
            if logic:
                break
    
    print(f'#{test+1} {logic}')