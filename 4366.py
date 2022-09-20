tc = int(input())
for  test in range(tc):
    num2 = list(input())
    num3 = list(input())
    num2 = list(map(int,num2))
    num3 = list(map(int,num3))
    temp2 = []
    temp3 = []

    for j in range(len(num2)):
        if num2[j]:
            num2[j] = 0
        else:
            num2[j] = 1
        num =0
        for i in range(len(num2)):
            num = num *2 + num2[i]
        temp2.append(num)
        if num2[j]:
            num2[j] = 0
        else:
            num2[j] = 1

    for j in range(len(num3)):
        if num3[j] == 1:
            temp = [0, 2]
            back = 1
        elif num3[j] == 0:
            temp = [1, 2]
            back = 0
        else:
            temp = [0,1]
            back =2
        for k in temp:
            num3[j] = k
            num =0
            for i in range(len(num3)):
                num = num *3 + num3[i]
            temp3.append(num)
        num3[j] = back
    ans = set(temp2)&set(temp3)
    ans = list(ans)[0]
    print(f'#{test+1} {ans}')