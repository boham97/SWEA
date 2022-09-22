dx = [-1,1,0,0]
dy = [0,0,-1,1]
tc = int(input())
for test in range(tc):
    N = int(input())
    atom = [[] for _ in range(N)]
    E = [0] * N
    for i in range(N):
        temp = list(map(int,input().split()))
        atom[i] = [temp[0],temp[1],temp[2]]
        E[i] = temp[3]
    used = [0]  * N
    ans = 0
    num = N
    while num:
        iter = num
        for i in range(iter):
            if atom[i][0] < -1000 or atom[i][0] >= 1000 and atom[i][1] < -1000 or atom[i][1] >= 1000:
                num -= 1
                used[i] = 1
            else:
                expect = (atom[i][0]+dx[atom[i][2]],atom[i][1]+dy[atom[i][2]])
                for j in range(4):
                    if [expect[0]+dx[j],expect[1]+dy[j],j] in atom:
                        