
test_case = int(input())

for test in range(test_case):
    num = int(input())
    temp = [[] for i in range(num)]
    for i in range(num):
        temp[i] = list(map(int,input().split()))
        core =[[],[]]
    for i in range(1, num-1):
        for j in range(1, num-1):
            if temp[i][j] == 1 :
                core[0].append(i)
                core[1].append(j)
    state = [0 for i in range(len(core[0]))]
    disable_state = [set() for i in range(len(core[0]))]
    maxcore = 0
    minwire = 0
    while(state[0] < 5):
        logic = 0
        for i in range(len(state)-1,-1,-1):
            if state[0] == 5:
                pass
            elif state[i] == 5:
                state[i] = 0
                state[i - 1] += 1
        
        for i in range(len(state)):
            if state[i] in disable_state[i]:
                state[i] += 1
                for j in range(i+1,len(state)):
                    state[j] = 0
                logic = 1
                break  
        if logic == 1:
            continue
        cnt = 0
        for i in state:
            if i == 0:
                cnt += 1
        if len(core[0]) - cnt < maxcore:
            state[len(state)-1] += 1
            continue

        cell=[[] for i in range(num)]
        for i in range(num):
            cell[i]= temp[i][:]

        for i in range(len(core[0])):
            if state[i] == 0:
                pass
            elif state[i] == 1:
                for j in range(core[1][i]+1,num):
                    if cell[core[0][i]][j] == 1:
                        logic = 1
                        disable_state[i].add(1)
                        break
                    if cell[core[0][i]][j] == 2:
                        logic = 1
                        break
                    cell[core[0][i]][j] += 2

            elif state[i] == 2:
                for j in range(core[0][i]+1,num):
                    if cell[j][core[1][i]] == 1:
                        logic = 1
                        disable_state[i].add(2)
                        break
                    if cell[j][core[1][i]] == 2:
                        logic = 1
                        break
                    cell[j][core[1][i]] += 2

            elif state[i] == 3:
                for j in range(core[1][i]):
                    if cell[core[0][i]][j] == 1:
                        logic = 1
                        disable_state[i].add(3)
                        break
                    if cell[core[0][i]][j] == 2:
                        logic = 1
                        break
                    cell[core[0][i]][j] += 2

            elif state[i] == 4:
                for j in range(core[0][i]):
                    if cell[j][core[1][i]] == 1:
                        logic = 1
                        disable_state[i].add(4)
                        break
                    if cell[j][core[1][i]] == 2:
                        logic = 1
                        break
                    cell[j][core[1][i]] += 2
            if logic == 1:
                logic = 0
                break
            
        else:
            core_num = 0
            wire_num = 0
            for i in state:
                if i != 0:
                    core_num += 1
            for i in range(num):
                for j in range(num):
                    if cell[i][j] == 2:
                        wire_num += 1
            if core_num > maxcore:
                maxcore = core_num
                minwire = wire_num
            elif core_num == maxcore and minwire > wire_num:
                minwire = wire_num
            #print(state)
            #print(disable_state)
            #print(cell, end= '   ')
            #print(maxcore, minwire)
            

        state[len(state)-1] += 1
    print(f'#{test+1} {minwire}')
