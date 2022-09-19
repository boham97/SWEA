# 이진탐색
tc = int(input())
for test in range(tc):
    N = int(input())
                        #2^10 = 1024 > 10^3
    for i in range(0,21):  # 2^60 > 10^18  
        if N <= 2**(3*i):
            rear = i
            break
    front = max(rear-1,0)
    
    ans = -1
    rear = 2**rear
    front = 2**front
    if rear**3 == N:
        ans = rear
    if front**3 == N:
        ans = front

    middle = (front+rear)//2
    print(front,rear)
    while 1:
        print(middle)
        if middle **3 < N:
            front = middle
        elif middle **3 > N:
            rear = middle
        else:
            ans = middle
            break
        middle = (front+rear)//2
        if front == middle or middle == rear:
            break

    print(f'#{test+1} {ans}')