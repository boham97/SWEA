test= int(input())

for z in range(test):
    logic= 0
    logic2= 0
    intinput = list(map(int,list(input())))
    numadd=[]
    print('#',end='')
    print(z+1,'',end='')
    minn=[]
    maxn=[]
    temp=[]

    for i in range(len(intinput)):
        minn.append(int(intinput[i]))
        maxn.append(int((intinput[i])))
    
    
    for i in range(len(minn)-1):
        if logic== 1:
            break
        minnum=min(minn[i+1:len(minn)])
        if minnum< minn[i] :
            for j in range(i+1,len(minn)):
                if minn[j]== minnum:
                    numadd.append(j)
            minn[i], minn[numadd[len(numadd)-1]]= minn[numadd[len(numadd)-1]], minn[i] 
            logic+=1
            
    if minn[0]==0 and intinput[0]==0:
        print('',end='')
    elif minn[0]==0 and intinput[0]!=0:
        minn[0], minn[numadd[len(numadd)-1]]= minn[numadd[len(numadd)-1]], minn[0]
        for i in range(1,len(minn)):
            if logic2==1:
                break
            if minn[i]!= 0:
                minn[i], minn[numadd[len(numadd)-1]]= minn[numadd[len(numadd)-1]], minn[i]
                logic2+=1       
            
    for i in minn:
        print(str(i),end='')
    print(end=' ')
    numadd=[]
    logic= 0
    

    for i in range(len(maxn)-1):
        if logic== 1:
            break
        maxnum=max(maxn[i+1:len(maxn)])
        if maxnum> maxn[i]:
            for j in range(i+1,len(maxn)):
                if maxn[j]== maxnum:
                    numadd.append(j)
            maxn[i], maxn[numadd[len(numadd)-1]]= maxn[numadd[len(numadd)-1]], maxn[i] 
            logic+=1
            
    for i in maxn:
        print(str(i),end='')
    print()





    
