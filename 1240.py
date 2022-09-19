pattern = [
    '0001101',
    '0011001',
    '0010011',
    '0111101',
    '0100011',
    '0110001',
    '0101111',
    '0111011',
    '0110111',
    '0001011',
]

tc = int(input())
for test in range(tc):
    N, M = map(int,input().split())
    buffer = [input() for _ in range(N)]
    ans = 0
    for i in range(N):
        if ans:
            break
        for j in range(M-56):
            if buffer[i][j:j+7] not in pattern:
                continue
            temp = [-1] * 8
            for k in range(8):
                for l in range(10):
                    if buffer[i][j+7*k:j+7*k+7] == pattern[l]:
                        temp[k] = l
            temp2 = 0
            for m in range(8):
                if m%2 == 0:
                    temp2 += temp[m] * 3
                else:
                    temp2 += temp[m]
            if temp2 % 10 == 0 and -1 not in temp:
                ans = sum(temp)
                break
    print(f'#{test+1} {ans}')