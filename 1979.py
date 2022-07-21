
testing_num=input()
for i in range(int(testing_num)):
    result= 0
    
    size, word=map(int,(input().split(' ')))
    matrix=[0 for k in range(size)]
    for j in range(size):
        buffer=input().rstrip()
        matrix[j]=list(map(int, buffer.split(' ')))

    for k in range(size):
        for j in range(size-word+1):
            if j==0 and sum(matrix[k][:word])==word and matrix[k][word]==0:
                result+=1
            elif j== size-word and sum(matrix[k][size-word:size])==word and matrix[k][size-word-1]==0:
                result+=1            
            elif sum(matrix[k][j:j+word])==word and matrix[k][j-1]==0 and matrix[k][j+word]==0:
                result+=1
    for k in range(size):
        for j in range(size-word+1):
            if j==0 :
                temp=0
                for n in range(word+1):
                    temp+=matrix[n][k]
                if temp==word and matrix[word][k]==0:
                    result+=1
            elif j== size-word:
                temp=0
                for n in range(size-word-1,size):
                    temp+=matrix[n][k]
                if temp==word and matrix[size-word-1][k]==0:
                    result+=1            
            else:
                temp=0
                for n in range(j-1,j+word+1):
                    temp+=matrix[n][k]
                if temp==word and matrix[j-1][k]==0 and matrix[j+word][k]==0:
                    result+=1
    print('#',end='')
    print(i+1,result)
