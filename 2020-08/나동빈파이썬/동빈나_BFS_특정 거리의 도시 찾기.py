#dfs인줄알고 풀었는데 bfs였음,,

n,m, k, x = map(int, input().split())
graph = []
for l in range(m):
    i,j = map(int, input().split())
    graph.append([i,j])

arr = []
arr.append(x)
def dfs(x, count):
    for i in range(len(graph)):
        #지금 있는곳에서 갈 수 있는곳
        if graph[i][0] == x:
            #처음 방문하는 곳일때
            if graph[i][1] not in arr:
                arr.append(graph[i][1])
                print(k,count+1)
                if k == count+1:
                    print(graph[i][1])
                dfs(graph[i][1], count + 1)
    return False

dfs(x, 0)