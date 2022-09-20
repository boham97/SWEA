tc = int(input())

for test in range(tc):
    N, buffer = input().split()
    N = int(N)
    ans = ''
    print(f'#{test+1}', end =' ')
    for s in buffer:
        temp = ''
        if 48 <= ord(s)<=57:
            num = int(s)
        elif 65 <= ord(s)<= 70:
            num = ord(s) - 55
        for i in range(4):
            temp += str(num%2)
            num = num//2
            ans += temp[::-1]
        print(temp[::-1],end='')
    print()
