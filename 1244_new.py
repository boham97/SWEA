def f():
    temp2 = 0
    for i in range(N):
        temp2 = temp2 *10 + arr[i]
    return temp2

def best():
    a = sorted(arr)
    return a[::-1]


def dfs(cnt):
    if cnt>0 and best_num[:min(cnt-1,N)] != arr[:min(cnt-1,N)]:
        return
    global ans
    if cnt == change:
        if ans < f():
            ans = f()
        return
    else:
        for i in range(N-1):
            for j in range(i+1,N):
                arr[i], arr[j] = arr[j], arr[i]
                dfs(cnt+1)
                arr[i], arr[j] = arr[j], arr[i]


tc = int(input())
for test in range(tc):
    buffer, change = input().split()
    arr = list(map(int, list(buffer)))
    N = len(arr)
    change = int(change)
    ans = -1
    best_num = best()
    cnt = [0] * 10
    many = 0
    last = [0,0]
    dfs(0)
    print(f'#{test+1} {ans}')