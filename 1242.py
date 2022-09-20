import sys
sys.stdin = open('1240.txt')
origin_pattern = [
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
#arr = ['0','1', '2', '3', '4', '5', '6', '7', '8', '9','A','B','C','D','E','F'] -> runtime error?
tc = int(input())
for test in range(tc):
    N, M = map(int,input().split())
    buffer = [input() for _ in range(N)]
    ans = 0
    anslist = []
    for i in range(N):
        two = ''
        ham = 0
        lastham = 0
        for s in buffer[i]:
            temp = ''
            if 48 <= ord(s)<=57:
                num = int(s)
            elif 65 <= ord(s)<= 70:
                num = ord(s) - 55
            for i in range(4):
                temp += str(num%2)
                ham += num%2
                num = num//2
            two += temp[::-1]
        if ham == 0:
            lastham = 0
            continue
        elif ham == lastham:
            continue
        h = 1
        while h<6: #4*M >56*h
            pattern = [''] *10
            for q in range(10):
                for w in range(7):
                    for _ in range(h):
                        pattern[q] += origin_pattern[q][w]
            #for j in range(4*M-len(origin_pattern[0])*8+1):
            j = 0
            while j < 4*M-len(origin_pattern[0])*8+1:
                if two[j:j+7*h] not in pattern :
                    j += 1
                    continue
                temp = [-1] * 8
                flag = 0
                for k in range(8):
                    for l in range(10):
                        if two[j+7*k*h:j+7*k*h+7*h] == pattern[l]:
                            temp[k] = l

                temp2 = 0
                for m in range(8):
                    if m%2 == 0:
                        temp2 += temp[m] * 3
                    else:
                        temp2 += temp[m]
                if temp2 % 10 == 0 and -1 not in temp and temp not in anslist:
                    ans += sum(temp)
                    anslist.append(temp)
                    break
                j += 1
            h += 1
    print(f'#{test+1} {ans}')