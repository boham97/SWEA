test= int(input())
for i in range(test):
    num=int(input())
    result=divmod(num,3)[0]
    print('#',end='')
    print(i+1,end=' ')
    print(result)
