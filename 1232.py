def f(x):
    if x == 0:
        return
    else:
        f(son1[x])
        num1 = saved[son1[x]]
        f(son2[x])
        num2 = saved[son2[x]]
        logic = saved[x]
        if logic == '+':
            saved[x] = num1 + num2
        elif logic == '-':
            saved[x] = num1 - num2
        elif logic == '*':
            saved[x] = num1 * num2
        elif logic == '/':
            saved[x] = num1 // num2
arr1 = ['+', '-', '*', '/']

for test in range(10):
    N = int(input())
    son1 = [0] * (N+1)
    son2 = [0] * (N+1)
    saved = [0] * (N+1)
    for i in range(N):
        buffer = list(input().split())
        node = int(buffer[0])
        if buffer[1] in arr1:
            saved[node] = buffer[1]
            son1[node], son2[node] = int(buffer[2]), int(buffer[3])
        else:
            saved[node] = int(buffer[1])
    f(1)
    print(f'#{test+1} {saved[1]}')