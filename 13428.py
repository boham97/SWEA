from itertools import combinations
test_case= int(input())

for test in range(test_case):
    temp = input()
    arr = list(map(int,list(temp)))
    arr_choose = list(range(len(arr)))
    maxinum = int(temp)
    mininum = int (temp)
    arr_combinations = list(combinations(arr_choose,2))
    for change in arr_combinations:
        if change[0] == 0 and arr[change[1]] == 0:
            pass
        else:
            arr[change[0]], arr[change[1]] = arr[change[1]], arr[change[0]]
            temp2 =''
            for i in arr:
                temp2 += str(i)
            temp2 = int(temp2)
            if temp2 < mininum:
                mininum = temp2
            if temp2 > maxinum:
                maxinum = temp2
            arr[change[0]], arr[change[1]] = arr[change[1]], arr[change[0]]
    print('#',end='')
    print(test+1,end=' ')
    print(mininum, maxinum)
