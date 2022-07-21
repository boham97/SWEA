empty= input()
for z in range(1,11):
    num, branch, son1, son2 = list(map(int,(input().split())))
    temp=input()
    arr= list(map(int,temp.split()))

    temp=[[],[]]
    for i in range(branch*2):
        if i%2==0:
            temp[0].append(arr[i])
            temp[1].append(arr[i+1])
    father1, father2= [son1],[son2]
    while(1):
        temp2=[]
        temp3=[]
        for i in range(branch):
            if temp[1][i] ==father1[len(father1)-1]:
                temp2.append(temp[0][i])
            if temp[1][i] ==father2[len(father2)-1]:
                temp3.append(temp[0][i])
        father1.extend(temp2)
        father2.extend(temp3)
        if len(set(father1)& set(father2))!= 0:
            a= list(set(father1)& set(father2))
            
            break
    ans=1
    temp4={a[0]}
    while(1):
        for i in range(branch):
            if temp[0][i] in temp4:
                temp4.add(temp[1][i])
        if ans<len(temp4):
            ans=len(temp4)
        else:
            break
    print('#',end='')
    print(z,end=' ')
    print(a[0],ans)

    
