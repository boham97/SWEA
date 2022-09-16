dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
tc = int(input())
for test in range(tc):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    ans = [0,0]
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                stack = [(i,j)]
                visited[i][j] = arr[i][j]
            while stack:
                x, y = stack[-1]
                for k in range(4):
                    x2 = x+dx[k]
                    y2 = y+dy[k]
                    if 0 <= x2 < N and 0 <= y2 < N and arr[x2][y2] == arr[x][y] + 1 and (visited[x2][y2] == 0 or (visited[x2][y2] != 0 and visited[x2][y2]>visited[x][y])):
                        visited[x2][y2] = visited[x][y]
                        stack.append((x2,y2))
                        if len(stack) > ans[1] or (len(stack) == ans[1] and ans[0]>arr[i][j]):
                            ans = [arr[i][j],len(stack)]
                        break
                else:
                    if stack:
                        stack.pop()
    print(f'#{test+1} {ans[0]} {ans[1]}')