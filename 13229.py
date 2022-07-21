test= int(input())
a={'MON':6, 'TUE':5, 'WED':4, 'THU':3, 'FRI':2, 'SAT':1,'SUN':7}
for i in range(test):
    temp=input()
    print('#',end='')
    print(i+1, end=' ')
    print(a[temp])
