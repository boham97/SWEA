test_case = int (input())

for test in range(test_case):
    minimum ,maximum, num = list(map(int,input().split(' ')))
    num_sample = list(map(int,input().split(' ')))
    
    print('#', end='')
    print(test + 1, end = ' ')
    for num in num_sample:
        logic = 0
        height1 = len(str(minimum)) - len(str(num))
        height2 = len(str(maximum)) - len(str(num))
        for height in range(height1,height2+1):
            test_num1 = [num * 10**height, (num +1) * 10**(height) - 1]
            test_num2 = [num * 10**height, (num +1) * 10**(height) - 1]     # 자리수가 같은경우, 자리수가 더큰겨웅 추가
            if test_num1[0] <= minimum and test_num1[1] >= minimum:
                logic += 1
            elif test_num1[0] <= maximum and test_num1[1] >= maximum:
                logic += 1
            elif test_num2[0] <= minimum and test_num2[1] >= minimum:
                logic += 1
            elif test_num2[0] <= maximum and test_num2[1] >= maximum:
                logic += 1
            elif test_num1[0] <= maximum and test_num1[1] >= minimum:
                logic += 1
            elif test_num2[0] <= maximum and test_num2[1] >= minimum:
                logic += 1

            
        if logic>0:
            print('O',end='')
        else:
            print('X', end= '')
    print()