num= int(input())
for i in range(1,num+1):
    logic= 0
    for j in str(i):
        if j=='3' or j=='6' or j=='9':
            logic+= 1
            print('-',end='')
    if logic== 0:
        print(i,end='')
    print(' ',end='')
