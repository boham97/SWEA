test= input()
for j in range(int(test)):
    length1, length2= input().split(' ')
    length1=int(length1)
    length2=int(length2)
    
    if length1> length2:
        arr2= list(input().split(' '))
        arr1= list(input().split(' '))
        length1, length2= length2, length1
    else:
        arr1= list(input().split(' '))
        arr2= list(input().split(' '))
    print('#',end='')
    print(j+1,end=' ')

    max=0
    for i in range(length2-length1+1):
        sum=0
        for j in range(length1):
            sum=sum+int(arr1[j])*int(arr2[i+j])
        if sum>max:
            max=sum
            a=i
            b=j
    print(max)
    