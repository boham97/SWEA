arr = [1] * 13
for i in range(1,13):
    arr[i] = arr[i-1]/2
#이진수2
tc = int(input())
for test in range(tc):
    num = float(input())
    i = 1
    ans = ''
    while num and i < 13:
        if num >= arr[i]:
            num -= arr[i]
            ans += '1'
        else:
            ans += '0'
        if num == 0:
            print(f'#{test+1} {ans}')
            break
        i += 1
    else:
        print(f'#{test+1} overflow')