test= int(input())
for z in range(test):
    logic=0
    num=int(input())
    mat=[['.' for i in range(num)] for j in range(num+10)]
    for j in range(num):
        mat[j+5]=list(input())
    for i in range(num+10):
        mat[i].append('.')
        mat[i].append('.')
        mat[i].append('.')
        mat[i].append('.')
        mat[i].append('.')
        mat[i].insert(0,'.')
        mat[i].insert(0,'.')
        mat[i].insert(0,'.')
        mat[i].insert(0,'.')
        mat[i].insert(0,'.')

    for i in range(num):
        for j in range(num):
            temp=['' for i in range(4)]
            if mat[i+5][j+5]== 'o':
                for k in range(5):
                    temp[0]+=mat[i+5+k][j+5]
                    temp[1]+=mat[i+5][j+5+k]
                    temp[2]+=mat[i+5+k][j+5+k]
                    temp[3]+=mat[i+5-k][j+5+k]
                if 'ooooo' in temp:
                    logic+=1
    print('#',end='')
    print(z+1,end=' ')
    if logic>0:
        print('YES')
    else:
        print('NO')
