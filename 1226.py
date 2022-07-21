for z in range(10):
    logic= 0
    mat=[0 for i in range(16)]
    pi= 0
    pj= 0
    last=0
    test= int(input())
    for i in range(16):
        mat[i]= list(map(int,list(input())))
        last+= sum(mat[i])
    for i in range(1,16):
            for j in range(1,16):
                if mat[i][j]== 3:
                    pi, pj= i,j
    print('#',end='')
    print(test,end=' ')
    while(logic==0):
        for i in range(1,16):
            for j in range(1,16):
                if mat[i][j]==2 and mat[i-1][j]== 0:
                    mat[i-1][j]= 2
                elif mat[i][j]==2 and mat[i][j-1]== 0:
                    mat[i][j-1]= 2
                elif mat[i][j]==2 and mat[i][j+1]== 0:
                    mat[i][j+1]= 2
                elif mat[i][j]==2 and mat[i+1][j]== 0:
                    mat[i+1][j]= 2

        present=0
        for i in range(16):
            present+= sum(mat[i])
        if last ==present:
            print(0)
            logic+=1
        if mat[pi+1][pj]==2 or mat[pi-1][pj]==2 or mat[pi][pj-1]==2 or mat[pi][pj+1]==2:
            print(1)
            logic+=1
        last= present
