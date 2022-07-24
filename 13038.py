test= int(input())
for z in range(test):
    min=0
    
    time= int(input())
    week= list(map(int,input().split(' ')))
    twoweek= week+week

    day, remain= divmod(time,sum(week))
    day= 7*(day-1)
    remain+= sum(week)

    minday=14
    for i in range(7):
        temp= 0
        for j in range(14-i):
            temp+=twoweek[i+j]
            if temp== remain:
                if j<minday:
                    minday=j
    print('#',end='')
    print(z+1,end=' ')
    print(day+minday+1)
