tc = int(input())
for test in range(tc):
    N, M = map(int, input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    home =[]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                home.append([i,j])
    ans = 0
    case = [[0]*(2*N+1) for _ in range(2)]
    for k in range(2*N+1):
        case[1][k] = -((k+1)**2) -(k)**2
    for i in range(N):
        for j in range(N):
            case[0] = [0]*(2*N+1)
            for x,y in home:
                case[0][abs(x-i)+abs(y-j)] += 1
            for k in range(2*N+1):
                if sum(case[0][:k+1]) > ans and M*sum(case[0][:k+1])+case[1][k]>=0:
                    ans = sum(case[0][:k+1])
    print(f'#{test+1} {ans}')