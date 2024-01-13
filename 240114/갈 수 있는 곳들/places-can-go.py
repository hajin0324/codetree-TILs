from collections import deque

n, k = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
visited = [
    [False] * n
    for _ in range(n)
]
q = deque()


def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n


def can_go(x, y):
    if not in_range(x, y):
        return False
    if grid[x][y] or visited[x][y]:
        return False
    return True


def bfs():
    global cnt
    dxs, dys = [0, 1, 0 ,-1], [1, 0, -1, 0]

    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            new_x, new_y = x + dx, y + dy
            
            if can_go(new_x, new_y):
                visited[new_x][new_y] = True
                q.append((new_x, new_y))


for _ in range(k):
    r, c = map(int, input().split())
    q.append((r - 1, c - 1))
    visited[r - 1][c - 1] = True

bfs()

cnt = 0
for i in range(n):
    for j in range(n):
        if visited[i][j]:
            cnt += 1
print(cnt)