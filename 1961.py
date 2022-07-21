test= input()
for k in range(int(test)):
    result=0
    size= int(input())
    mat=[0 for i in range(size)]
    for i in range(size):
        buffer=input().rstrip()
        mat[i]=list(map(int, buffer.split(' ')))
    print('#',end='')
    print(k+1)
    for i in range(size):
        for j in range(size):
            print(mat[size-j-1][i],end='')
        print(end=' ')
        for j in range(size):
            print(mat[size-i-1][size-j-1],end='')
        print(end=' ')
        for j in range(size):
            print(mat[j][size-i-1],end='')
        print('')            
