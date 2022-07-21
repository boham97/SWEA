test= int(input())

for z in range(test):
    logic= 15
    S = input()
    for i in S:
        if i=='x':
            logic-=1

    print('#',end='')
    print(z+1,'',end='')
    if logic>=8:
        print('YES')
    else:
        print('NO')
