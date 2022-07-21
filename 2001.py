test= input()
for i in range(int(test)):
    result=0
    size, attack=map(int,(input().split(' ')))
    matrix=[0 for j in range(size)]
    for j in range(size):
        buffer=input().rstrip()
        matrix[j]=list(map(int, buffer.split(' ')))
    for j in range(size-attack+1):
        for k in range(size-attack+1):
            temp=0;
            for l in range(attack):
                temp+=sum(matrix[j+l][k:k+attack])
            if result<temp:
                result= temp
    print('#',end='')
    print(i,result)
