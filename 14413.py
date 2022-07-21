jud_x=None
jud_y=None

test=int(input())
for z in range(test):
    logic='possible'
    jud_x=None
    jud_y=None
    x,y= list(map(int,input().split(' ')))
    mat=[0 for i in range(x)]

    for i in range(x):
        mat[i]= list(input())

    for i in range(x):
        for j in range(y):
            if mat[i][j]!='?':
                jud_x=i
                jud_y=j
                break
    
    for i in range(x):
        if jud_x==None:
            break
        for j in range(y):
            if (i+j)%2==(jud_x+jud_y)%2 and mat[i][j]!= mat[jud_x][jud_y] and mat[i][j]!= '?':
                logic='impossible'
                
            if (i+j)%2!=(jud_x+jud_y)%2 and mat[i][j]== mat[jud_x][jud_y] and mat[i][j]!= '?':
                logic='impossible'

    print('#',end='')
    print(z+1, logic)
