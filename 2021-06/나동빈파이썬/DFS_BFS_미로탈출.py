from collections import deque

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    # 큐가 빌때까지 반복
    while queue:
        x,y = queue.popleft()
        # 상하좌우
        for i in range(4):
            nx = i+dx[i]
            ny = i+dy[i]
            # 맵을 넘어가는 경우 제외
            if nx <0 or ny <0 or nx >= n or ny >= m:
                continue
            # 괴물 있는경우 제외
            if graph[nx][ny] == 0:
                continue
            # 안전한길이면 1 추가해서 지나갔다고 알려줌
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y]+1
                # 그부분부터 다시 시작
                queue.append((nx,ny))
        return graph[n-1][m-1]

print(bfs(0,0))