test=int(input())
compare=[1,2,3,4,5,6,7,8,9]
logic=1
temp=[0 for i in range(9)]
for k in range(test):
    mat=[0 for i in range(9)]
    for i in range(9):
        mat[i]= list(map(int,input().split(' ')))
        if compare!=sorted(mat[i]):
            logic=0
    for i in range(0,9,3):
        for j in range(0,9,3):
            for l in range(3):
                for m in range(3):
                    temp.remove(temp[0])
                    temp.append(mat[i+l][j+m])
            
            if compare!=sorted(temp):
                logic=0
    for i in range(9):
        for j in range(9):
            temp.remove(temp[0])
            temp.append(mat[j][i])
        if compare!=sorted(temp):
            logic=0
    if logic==1:
        print('#',end='')
        print(k+1,1)
    else:
        print('#',end='')
        print(k+1,0)
    logic=1
