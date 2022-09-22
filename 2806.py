def f(i, N):
    global ans
    if i == N:
        ans += 1
        #print(ans)
        return
    else:
        for j in range(i, N):
            mat[i], mat[j] = mat[j], mat[i]
            for k in range(i):
                if abs(k-i) == abs(mat[k]- mat[i]):
                    break
            else:
                f(i+1,N)
            mat[i], mat[j] = mat[j], mat[i]
tc = int(input())
for test in range(tc):
    N = int(input())
    ans = 0
    mat = list(range(N))
    f(0,len(mat))
    print(f'#{test+1} {ans}')