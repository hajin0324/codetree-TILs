OFFSET = 100
MAX_R = 200

n = int(input())
grid = [
    [0 for _ in range(MAX_R + 1)]
    for _ in range(MAX_R + 1)
]

for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    x1, y1, x2, y2 = x1 + OFFSET, y1 + OFFSET, x2 + OFFSET, y2 + OFFSET
    for i in range(x1, x2):
        for j in range(y1, y2):
            grid[i][j] += 1

cnt = 0
for i in range(MAX_R + 1):
    for j in range(MAX_R + 1):
        if grid[i][j] >= 1:
            cnt += 1
print(cnt)