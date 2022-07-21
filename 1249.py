test= int(input())

for z in range(1,test+1):
    num= int(input())
    mat=[0 for i in range(num)]
    ans=[[0 for i in range(num)] for j in range(num)]
    for i in range(num):
        mat[i]= list(input())
        mat[i]=list(map(int,mat[i]))
    
    for i in range(1,num):
        ans[i][0]=ans[i-1][0]+ mat[i][0]
        ans[0][i]=ans[0][i-1]+ mat[0][i]

    for i in range(1,num):
        for j in range(1,num):
            minimum= min(ans[i-1][j],ans[i][j-1])
            ans[i][j]+= minimum+ mat[i][j]
    print(ans[num-1][num-1])
