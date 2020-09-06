import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)#무한을 의미

#노드의 개수 간선의 개수 입력받기
n,m = map(int, input().split())
#시작노드 번호를 입력받기
start = int(input())
#각 노드에 연결 되어있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for i in range(n+1)]
#방문한 적이 있는지 체크하는 리스트 만들기
visited = [False]*(n+1)
#최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)

#모든 간선 정보 입력받기
for _ in range(m):
    a,b,c = map(int, input().split())
    #a번 노드에서 b번노드로 가는 비용이 c라는 의미
    graph[a].append((b,c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    #시작 노드를 초기
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


#다익스트라 알고리즘 수핼
dijkstra(start)

#모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n+1):
    if distance[i] == INF:#도달할수 없는 경우
        print('INFINITY')
    else:#도달 가능하면 거리 출력
        print(distance[i])