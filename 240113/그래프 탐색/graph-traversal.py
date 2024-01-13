n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
cnt = 0

def dfs(vertex):
    global cnt

    for curr_v in graph[vertex]:
        if not visited[curr_v]:
            cnt += 1
            visited[curr_v] = True
            bfs(curr_v)


for _ in range(m):
    x, y = tuple(map(int, input().split()))
    graph[x].append(y)
    graph[y].append(x)

visited[1] = True
dfs(1)

print(cnt)