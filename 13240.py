test_case= int(input())

for test in range(test_case):
    x, y, num = list(map(int,input().split()))
    temp = list(input().split())
    long = list(len(i) for i in temp)
    minlong = max(long)
    maxsize = 1
    best = 0
    for size in range(minlong, sum(long)+len(long)):
        word = 0
        temp = 0
        line = 1
        while(word < len(long)):
            if temp == 0:
                temp += long[word]
                word += 1
            elif temp + long[word] + 1 <= size:
                temp += long[word] + 1
                word += 1
            else:
                temp = 0
                line += 1
        if min((x//line),(y//size)) > best:
            best = min((x//line),(y//size))
    print('#', end='')
    print(test + 1, end = ' ')
    print (best)