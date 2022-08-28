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
    cnt = 0
    for i in range(2,x+4):
        if mat[i-2] < mat[i] and mat[i-1] < mat[i] and mat[i+1] < mat[i] and mat[i+2] < mat[i]:
            temp = [mat[i]-mat[i-2], mat[i]-mat[i-1], mat[i]-mat[i+1], mat[i]-mat[i+2]]
            min_temp = temp[0]
            for i in temp:
                if i < min_temp:
                    min_temp = i
            cnt += min_temp
    print('#',end='')
    print(z+1, cnt)
