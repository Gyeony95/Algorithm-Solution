n, m = map(int, input().split())
# 이차원 배열 0으로 초기화
d = [[0] * m for _ in range(n)]
x,y,direction = map(int, input().split())

d[x][y] = 1 #현재좌표 방문처리

array = []

# 맵 정보 입력 받기
for i in range(n):
    array.append(list(map(int,input().split())))
dx = [-1,0,1,0] # 북동서남
dy = [0,1,0,-1]

# 왼쪽으로 회전처리
def left_turn():
    global direction
    direction -= 1
    if direction ==-1:
        direction = 3

# 시뮬레이션 시작
count = 1
turn_time = 0
while True:
    left_turn()#한번 돌리고 시작
    # 임시 좌표 설정
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 임시좌표가 0이고 방문기록도 없는경우
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] =1
        x = nx
        y = ny
        count +=1
        turn_time = 0
        continue
    else:
        turn_time +=1

    if turn_time == 4:
        nx = x -dx[direction]
        ny = y-dy[direction]
        if array[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0

print(count)