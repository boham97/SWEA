from collections import deque
for test in range(10):
    N, front = map(int, input().split())
    arr = list(map(int,input().split()))
    
    relation = [[],[]]
    relation[0] = [0] * 101
    relation[1] = [[0] for _ in range(101)]
    for i in range(N//2):
        relation[1][arr[2*i]].append(arr[2*i+1])
    deq = deque()
    deq.append(front)
    relation[0][front] = 1
    day = 2
    while deq:
        temp = deq.popleft()
        for next in relation[1][temp]:
            if relation[0][next] == 0:
                deq.append(next)
                relation[0][next] = relation[0][temp] + 1
    last = max(relation[0])

    ans = 0
    for i in range(1,101):
        if relation[0][i] == last:
            ans = i
    print(f'#{test+1} {ans}')