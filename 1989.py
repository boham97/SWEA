def solver(txt):
    if ' ' in txt:
        temp=txt.replace(' ','')
        txt=temp
    temp= txt[::-1]

    if temp==txt:
        return 1
    else:
        return 0

T = int(input())
arr=[]
for i in range(T):
    arr.append(input())


for i in range(T):
    print('#',end='')
    print(i+1,end=' ')
    result= solver(arr[i])
    print(result)
