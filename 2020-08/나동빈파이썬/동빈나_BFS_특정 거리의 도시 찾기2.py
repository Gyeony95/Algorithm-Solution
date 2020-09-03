#모범답안
from _collections import deque
n,m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
for l in range(m):
    i,j = map(int, input().split())
    graph[i].append(j)

distance = [-1] *(n+1)
distance[x] = 0#출발점

q = deque([x])

while q:
    now = q.popleft()
    #현재 도시에서 이동할 수 있는 모든 도시 확인
    for next_node in graph[now]:
        #아직 방문하지 않은 도시라면
        if distance[next_node] == -1:
            distance[next_node] = distance[now] + 1
            q.append(next_node)

check = False
#최단거리가 k인 모든 노드를 오름차순으로 출력
for i in range(1, n+1):
    if distance[i] == k:
        print(i)
        check = True
if check == False:
    print(-1)

