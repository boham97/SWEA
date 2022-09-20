T = int(input())
for test in range(T):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]
    answer = 0
    for i in range(N):
        for j in range(N):
            for P in range(1,N-j):
                for K in range(N-i-P-1,0,-1):
                    ans = []
                    if 0 <= j-K and j+P<N:
                        ans.append(mat[i][j])
                        for p in range(1,P+1):
                            ans.append(mat[i+p][j+p])
                        for k in range(1,K+1):
                            ans.append(mat[i+P+k][j+P-k])
                        for p in range(1,P+1):
                            ans.append(mat[i+P+K-p][j+P-K-p])
                        for k in range(1,K):
                            ans.append(mat[i+K-k][j-K+k])
                        if len(ans) == len(set(ans)) and len(ans) > answer:
                            answer = len(ans)
    if answer:
        print(f'#{test+1} {answer}')
    else:
        print(f'#{test+1} -1')
