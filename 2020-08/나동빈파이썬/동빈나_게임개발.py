#지도의 크기를 할당받
n,m = map(int, input().split())

#리스트 컴프리헨션 방식
#방문한 위치를 저장받기위한 맵을 생성하고 0으로 초기화
d = [[0]*m for _ in range(n)]

#나의 위치 x,y와 바라보는 방향 direction을 할당받
x,y,direction = map(int, input().split())
#현재 좌표 방문처리
d[x][y] = 1

#지도 받
arr =[]
for i in range(n):
    arr.append(list(map(int,input().split())))

#북동서남의 방향을 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def left_turn():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

#시뮬레이션 시작
count = 1
turn_time = 0
while True:
    #왼쪽으로 회전
    left_turn()
    nx = x + dx[direction]
    ny = y + dy[direction]
    #회전 이후에 장먄에 가보지 않은 칸이 존재할 경우 이동
    if d[nx][ny] == 0 and arr[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    #회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time += 1
    #네방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        #뒤로 갈 수 있으면 이동하기
        if arr[nx][ny] == 0:
            x = nx
            y = ny
        #뒤가 바다로 막혀있는 경우
        else:
            break
        turn_time = 0

print(count)


