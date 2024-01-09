OFFSET = 100
MAX_R = 200

n = int(input())
rect = [
    [0 for _ in range(MAX_R)]
    for _ in range(MAX_R)
]

for i in range(1, n + 1):
    x1, y1, x2, y2 = map(int, input().split())
    x1, y1, x2, y2 = x1 + OFFSET, y1 + OFFSET, x2 + OFFSET, y2 + OFFSET

    for x in range(x1, x2):
        for y in range(y1, y2):
            rect[x][y] = i

area = 0
for i in range(MAX_R):
    for j in range(MAX_R):
        if rect[i][j] >= 2 and rect[i][j] % 2 == 0:
            area += 1
print(area)