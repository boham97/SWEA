test_case = int (input())

for test in range(test_case):
    minimum ,maximum, num = list(map(int,input().split(' ')))
    num_sample = list(map(int,input().split(' ')))
    
    print('#', end='')
    print(test + 1, end = ' ')
    for num in num_sample:
        logic = 0
        heightmax = len(str(maximum)) - len(str(num))
        for height in range(0, heightmax+1, 1):
            test_num = [num * 10**height, (num +1) * 10**(height) - 1]
            if test_num[0] <= minimum and test_num[1] >= minimum:
                logic += 1
            elif test_num[0] <= maximum and test_num[1] >= maximum:
                logic += 1
            elif test_num[0] <= maximum and test_num[1] >= maximum:
                logic += 1
            elif test_num[0] <= minimum and test_num[1] >= maximum:
                logic += 1
            elif test_num[0] >= minimum and test_num[1] <= maximum:
                logic += 1
        if logic>0:
            print('O',end='')
        else:
            print('X', end= '')
    print()