n, m = map(int, input().split())
colored = [
    [0 for _ in range(n)]
    for _ in range(n)
]

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]


def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n


for _ in range(m):
    r, c = map(int, input().split())
    r, c = r - 1, c - 1
    colored[r][c] = 1
    
    cnt = 0
    for dx, dy in zip(dxs, dys):
        nx, ny = r + dx, c + dy
        if in_range(nx, ny) and colored[nx][ny] == 1:
            cnt += 1

    if cnt == 3:
        print(1)
    else:
        print(0)