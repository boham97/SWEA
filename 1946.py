test= input()
for j in range(int(test)):
    num= int(input())
    long=0;
    print('#',end='')
    print(j+1)
    for i in range(num):
        alpha, many= input().split(' ')
        for j in range(int(many)):
            print(alpha, end='')
            long=long+1
            if long==10:
                print('')
                long=long-10
    print('')
