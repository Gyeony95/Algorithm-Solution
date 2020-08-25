from collections import deque
#내 답 중도 포기
n,m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

def bfs(x,y, pre):
    queue = deque()
    if graph[x][y] == 1:
        graph[x][y] = graph[x][y] + pre
    if graph[x+1][y] == 1 and x+1 <= m:
        queue.append((x+1,y))
    if graph[x-1][y] == 1 and x-1 >= 0:
        queue.append((x-1,y))
    if graph[x][y+1] == 1 and y+1 <= n:
        queue.append((x,y+1))
    if graph[x][y-1] == 1 and y-1 >= 0:
        queue.append((x,y-1))
    while queue:
        queue.popleft()


