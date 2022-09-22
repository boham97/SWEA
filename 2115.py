
tc = int(input())
for test in range(tc):
    N, M, C = map(int,input().split())
    GGUL = [list(map(int,input().split())) for _ in range(N)]
    value = [[0]*N for _ in range(N)]
    bubun = []
    bit = [0] * M
    for i in range(2**M-1):
        bit[0] += 1
        for j in range(M):
            if bit[j] == 2:
                bit[j] = 0
                bit[j+1] += 1
        bubun.append(bit[:])
    for i in range(N):
        for j in range(N-M+1):
            for logic in bubun:
                temp_value = 0
                temp_honey = 0
                for k in range(M):
                    temp_value += (GGUL[i][j+k]*GGUL[i][j+k]*logic[k])
                    temp_honey += GGUL[i][j+k]*logic[k]
                if temp_honey <= C and temp_value >value[i][j]:
                    value[i][j] = temp_value
    max_honey = 0
    for i in range(N**2-M):
        for j in range(i+M, N**2):
            temp2 = value[i//N][i%N]
            temp2 += value[j//N][j%N]
            if temp2 > max_honey:
                max_honey =temp2
    print(f'#{test+1} {max_honey}')