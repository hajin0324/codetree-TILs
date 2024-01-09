OFFSET = 100
MAX_R = 200

n = int(input())
rect = [
    [0 for _ in range(MAX_R + 1)]
    for _ in range(MAX_R + 1)
]

for _ in range(n):
    x1, y1 = map(int, input().split())
    x1, y1 = x1 + OFFSET, y1 + OFFSET

    for i in range(x1, x1 + 8):
        for j in range(y1, y1 + 8):
            rect[i][j] = 1

area = 0
for i in range(MAX_R + 1):
    for j in range(MAX_R + 1):
        if rect[i][j] == 1:
            area += 1   
print(area)