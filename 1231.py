def f(num):
    if num:
        f(son1[num])
        print(string[num], end='')
        f(son2[num])
for test in range(10):
    N = int(input())
    son1 = [0] * (N+1)
    son2 = [0] * (N+1)
    string = [0] * (N+1)
    for i in range(1,N+1):
        temp = list(input().split())
        for j in range(2,len(temp)):
            papa, son =int(temp[0]), int(temp[j])
            if son1[papa]:
                son2[papa] = son
            else:
                son1[papa] = son
        string[i] = temp[1]
    print(f'#{test+1}', end= ' ')
    f(1)
    print()
