def find(num):
    if arr[num] == num:
        return num
    else:
        return find(arr[num])


def union(num1, num2):
    arr[find(num2)] = find(num1)


tc = int(input())
for test in range(tc):
    V, E = map(int,input().split())
    graph = list()
    for i in range(E):
        a,b,c = map(int,input().split())
        graph.append([c,a,b])
    graph.sort()
    arr = list(range(V+1))
    ans = 0
    for i,j,k in graph:
        if find(j) != find(k):
            union(j,k)
            ans += i
    print(f'#{test+1} {ans}')