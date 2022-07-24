test_case = int(input())

for test in range(test_case):
    arr = list(input())
    robot = [0, 0]
    angles = [[1,0],[0,1],[-1,0],[0,-1]]
    angle = 0

    for i in arr:
        if i == 'L':
            angle += 1
            if angle == 4:
                angle = 0
        elif i == 'R':
            angle -= 1
            if angle == -1:
                angle = 3
        elif i == 'S':
            robot[0] = robot[0] + angles[angle][0]
            robot[1] = robot[1] + angles[angle][1]
    #print(robot, angle)
    if angle == 0 and (robot[0] !=0 or robot[1] != 0):
        result = 'oo'
    else:
        maxi = 0
        for i in range(4):
            for j in arr:
                if j == 'L':
                    angle += 1
                    if angle == 4:
                        angle = 0
                elif j == 'R':
                    angle -= 1
                    if angle == -1:
                        angle = 3
                elif j == 'S':
                    robot[0] = robot[0] + angles[angle][0]
                    robot[1] = robot[1] + angles[angle][1]
                    temp = robot[0]**2 + robot[1]**2

                    if temp > maxi:
                        maxi = temp
        result = maxi
    print('#',end='')
    print(test+1,'',end='')
    print(result)