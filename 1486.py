from itertools import combinations
test_num =int(input())

for test in range(test_num):
    num, length = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    arr.sort()
    
    max = sum(arr)
    min = max
    
    for i in range(0,num,1):
        if sum(arr[i::]) < length:
            break
        arr_combinations = list(combinations(arr,num - i))
        for j in arr_combinations:
            if sum(j)<min and sum(j) >= length:
                min =sum(j)
                best = j
    print('#',end= '')
    print(test +1, end=' ')
    print(min - length)