n = int(input())
k = int(input())
apple = []
for i in range(k):
    x, y = map(int, input().split())
    apple.append((x-1,y-1))
print(apple)
move = []
l = int(input())
for i in range(l):
    x, y = input().split()
    move.append([x,y])

arr = [[0 for col in range(n)] for row in range(n)]
snake = [(0,0)]
direct = [(0,1),(1,0),(0,-1),(-1,0)]
state = 0

count = 0
while True:
    count +=1
    previous = tuple(sum(elem) for elem in zip(snake[-1], direct[state]))
    print(previous)
    if snake in previous:
        print(count)
        break
    if previous[0] == n or previous[1] == n or previous[0] == -1 or previous[1] == -1:
        print(count, previous, snake)
        break
    snake.append(previous)#튜플끼리 더한거 원소 추가
    print(apple, previous)
    if apple in previous:
        pass
    else:
        snake.pop(0)
    if len(move) != 0:
        if count == int(move[0][0]):
            if move[0][1] == 'D':
                if state == 3:
                    state = 0
                else:
                    state += 1
            elif move[0][1] == 'L':
                if state == 0:
                    state = 3
                else:
                    state -= 1
            move.pop(0)
    else:
        pass



