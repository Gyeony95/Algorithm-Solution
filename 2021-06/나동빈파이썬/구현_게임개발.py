n, m = map(int, input().split())
a,b,d = map(int,input().split())
mMap = [[int(x) for x in input().split()] for _ in range(m)]

state = [a,b]


go = [[-1, 0], [0, 1], [1,0], [0, -1]]
count = 0
turn_count = 0

def turn(num):
    if num == 3:
        return 0
    else:
        return num+1

while True:
    if turn_count == 4:
        if mMap[state[0] + go[d][0]*-1][ state[1] + go[d][1]*-1] == 1:
            break
        elif (mMap[state[0] + go[d][0]*-1][ state[1] + go[d][1]*-1] == 0) or (mMap[state[0] + go[d][0]*-1][ state[1] + go[d][1]*-1] == 2):
            turn_count = 0
            count += 1
            mMap[state[0]][ state[1]] = 2
            state[0] = state[0] + go[d][0]*-1
            state[1] = state[1] + go[d][1]*-1
    d = turn(d)
    if (mMap[state[0] + go[d][0]][ state[1] + go[d][1]] == 1) or (mMap[state[0] + go[d][0]][ state[1] + go[d][1]] == 2):
        turn_count +=1
    elif mMap[state[0] + go[d][0]][ state[1] + go[d][1]] == 0:
        turn_count = 0
        count +=1
        mMap[state[0]][state[1]] = 2
        state[0] = state[0] + go[d][0]
        state[1] = state[1] + go[d][1]

print(count)


