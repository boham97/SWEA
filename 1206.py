for z in range(10):
    count=0

    x=int(input())
    y=input().rstrip()
    mat=[]
    mat= list(map(int,y.split(' ')))

    mat.insert(0,mat[0])
    mat.insert(0,mat[0])
    mat.append(mat[len(mat)-1])
    mat.append(mat[len(mat)-1])

    for i in range(2,x+4):
        if mat[i-2]<mat[i] and mat[i-1]<mat[i] and mat[i+1]<mat[i] and mat[i+2]<mat[i]:
            count+=min(mat[i]-mat[i-2],mat[i]-mat[i-1],mat[i]-mat[i+1],mat[i]-mat[i+2])
    print('#',end='')
    print(z+1, count)
