test= int(input())

for z in range(test):
    logic=0

    num=int(input())
    b=list(map(int,list(str(num))))
    b.sort()
    for i in range(2,10):
        if len(str(i*num))>len(str(num)):
            break
        a=list(map(int,list(str(i*num))))
        a.sort()
        if a== b:
            logic=1
        print(a,b)
    print('#',end='')
    print(z+1,'',end='')
    if logic==1:
        print('possilble')
    else:
        print('impossible')
