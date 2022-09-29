def find(num):
    if arr[num] == num:
        return num
    else:
        return find(arr[num])


def union(num1, num2):
    arr[find(num2)] = find(num1)


tc = int(input())
for test in range(tc):
    N, M = map(int, input().split())
    buffer = list(map(int, input().split()))
    arr = list(range(N+1))
    for i in range(M):
        union(buffer[2*i], buffer[2*i+1])
    ans_list = set()
    for i in range(1, N+1):
        ans_list.add(find(i))
    print(f'#{test+1} {len(ans_list)}')
