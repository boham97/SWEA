test= int(input())
for z in range(test):
    min=0
    
    time= int(input())
    week= list(map(int,input().split(' ')))
    min_day = time * 7
    for i in range(7):
        if week[i] == 1:
            learned = 0
            day = 0
            while(learned < time):
                learned += week[(i + day )%7]
                day +=1
                #print(day, learned)
            if day < min_day:
                min_day = day
    print('#',end='')
    print(z+1,'',end='')
    print(min_day)
