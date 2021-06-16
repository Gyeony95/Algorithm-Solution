n = int(input())
mList = list(map(str, input().split()))
start = [1,1]
for i in range(6):
    if mList[i] == 'R':
        if start[1] !=5:
            start[1] = start[1]+1
    elif mList[i] == 'L':
        if start[1] !=1:
            start[1] = start[1]-1
    elif mList[i] == 'U':
        if start[0] !=1:
            start[0] = start[0]-1
    elif mList[i] == 'D':
        if start[0] !=5:
            start[0] = start[0]+1

print(start[0], end=' ')
print(start[1], end='')
