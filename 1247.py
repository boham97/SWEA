import math
import random
from math import inf


#test= int(input())
for z in range(11):
    n=int(input())
    nant=100
    rho=0.05
    min=inf
    minroot=[]
    phe=[[0 for i in range(n+2)] for i in range(n+2)]
    cost=[[0 for i in range(n+2)] for i in range(n+2)]
    temp=list(input().split())
    temp=list(map(int,temp))
    x=[]
    y=[]
    for i in range(2*n+4):
        if i%2==0:
            x.append(temp[i])
            y.append(temp[i+1])
    for i in range(n+2):
        for j in range(n+2):
            if i==j:
                phe[i][j]= 0 
                cost[i][j]= inf
            else:
                phe[i][j]= 0.05
                cost[i][j]= abs(x[i]-x[j])+abs(y[i]-y[j])

    for iter in range(100):
        ant=[[1, 0] for i in range(nant)]
        p=[[0 for j in range(n+3)] for j in range(n+2)]
        for i in range(nant):
            for j in range(n+2):
                for k in range(0,n+2):
                    p[j][k+1]=phe[j][k]/cost[j][k]
                    if k==1 or k==0:
                        p[j][k+1]= 0
                #p[j]= list(map(lambda x:x/sum(p[j]),p[j]))
                    
            for j in range(2,n+2):
                next= random.uniform(0,sum(p[j]))
                for k in range(n+2):
                    if sum(p[j][0:k+1])<next and next< sum(p[j][0:k+2]):
                        ant[i].append(k)
                        for l in range(n+2):
                            p[l][k+1]=0




        for i in range(nant):
            ant[i].remove(1)
            ant[i].append(1)
            temp2= 0
            for j in range(n+2):
                phe[j]= list(map(lambda x:x*(1-rho),phe[j]))
            for j in range(n+1):
                temp2+= cost[ant[i][j]][ant[i][j+1]] 
            for j in range(n+1):
                phe[ant[i][j]][ant[i][j+1]]+=1/temp2
            ant[i].insert(0,temp2)
            


        ant.sort()
        if ant[0][0]<min:
            min= ant[0][0]
            minroot=list(ant[0][1:])
print(min, minroot)
        #print(phe)
            
            
                

                



    
