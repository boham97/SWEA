from itertools import combinations
tc = int(input())
for test in range(tc):
    N,M,C = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    mx =0
    for i in range(N**2 -1):
        if i//N != (i+M-1)//N:
            continue
        honey_list = []
        for k in range(M):
            honey_list.append(arr[(i+k)//N][(i+k)%N])
        tempmx1 = 0
        for n in range(1,M+1):
            for honey in combinations(honey_list, n):
                if sum(honey)<= C:
                    temp1 = 0
                    for k in range(n):
                        temp1 += honey[k] **2
                    if tempmx1 < temp1:
                        tempmx1 = temp1
        for j in range(i+M,N**2):
            if j//N != (j+M-1)//N:
                continue
            honey_list = []
            tempmx2 = 0
            for k in range(M):
                honey_list.append(arr[(j+k)//N][(j+k)%N])
            for n in range(1,M+1):
                for honey in combinations(honey_list, n):
                    if sum(honey)<= C:
                        temp2 = 0
                        for k in range(n):
                            temp2 += honey[k] **2
                        if tempmx2 < temp2:
                            tempmx2 = temp2
            if tempmx2 + tempmx1 > mx:
                mx = tempmx1 + tempmx2
    
    print(f'#{test+1} {mx}')