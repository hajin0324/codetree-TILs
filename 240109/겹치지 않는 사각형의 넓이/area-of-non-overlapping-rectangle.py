OFFSET = 1000
MAX_R = 2000

grid = [
    [0 for _ in range(MAX_R + 1)]
    for _ in range(MAX_R + 1)
]

for n in range(2, -1, -1):
    x1, y1, x2, y2 = map(int, input().split())
    x1, y1 = x1 + OFFSET, y1 + OFFSET
    x2, y2 = x2 + OFFSET, y2 + OFFSET

    for i in range(x1, x2):
        for j in range(y1, y2):
            grid[i][j] = n

area = 0
for i in range(MAX_R + 1):
    for j in range(MAX_R + 1):
        if grid[i][j] != 0:
            ans += 1

print(area)