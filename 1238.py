for z in range(1,11):
    num, start= list(map(int,(input().split())))
    temp=input()
    arr= list(map(int,temp.split()))
    temp2= list(set(arr))
    ans={}
    for i in temp2:
        ans[i]= 0
    ans[start]= 1
    iter= 2
    
    while(1):
        logic=0
        temp4=[]
        for i in range(0,num,2):
            if ans[arr[i]]!=0 and ans[arr[i+1]]==0:
                temp4.append(arr[i+1])
                logic+=1
        if logic==0:
            break
        for i in temp4:
            ans[i]=iter
        iter+=1
        
    iter-=1
    temp3=[]
    for i in temp2:
        if ans[i]==iter:
            temp3.append(i)
    print('#',end='')
    print(z,end=' ')
    print(max(temp3))
