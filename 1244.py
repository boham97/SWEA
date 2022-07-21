test= int(input())
for z in range(test):
    temp0=[]
    temp1=[]
    num, chance=list(input().split(' '))
    mat=list(map(int,str(num)))
    chance=int(chance)
    best=[0 for i in range(len(mat))]
    for i in range(len(mat)):
        best[i]= mat[i]
    best.sort(reverse=True)

    lastnum= 0
    combo= 1

    if mat!=best:
        for j in range(len(mat)-1):
            if chance==0:
                break
            if mat== best:
                break
            
            maxnum= mat[j]
            maxadd= j
            logic=0
            for k in range(j+1,len(mat)):
                if mat[k]>= maxnum:
                    maxnum= mat[k]
                    maxadd= k
                    logic=1
            if logic==1:
                mat[j], mat[maxadd]=mat[maxadd],mat[j]
                temp0.append(maxadd)
                temp1.append(mat[maxadd])
                chance=chance-1
                if lastnum==maxnum:
                    combo+= 1
                    temp1.sort()
                    for l in range(len(temp0)-combo,len(temp0)):
                        mat[temp0[l]]=temp1[l]
                    combo=1
                lastnum=maxnum
    if mat==best:
        for j in range(chance):
            if len(set(mat))!=len(mat) and mat==best:
                break
            else:
                mat[len(mat)-2], mat[len(mat)-1]= mat[len(mat)-1], mat[len(mat)-2]
    result=''.join(map(str,mat))
    print('#',end='')
    print(z+1, result)

