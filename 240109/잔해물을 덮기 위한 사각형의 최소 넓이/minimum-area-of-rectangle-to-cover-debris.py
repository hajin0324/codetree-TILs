OFFSET = 1000
MAX_R = 2000

checked = [
    [0 for _ in range(MAX_R + 1)]
    for _ in range(MAX_R + 1)
]

for n in range(1, 3):
    x1, y1, x2, y2 = map(int, input().split())
    x1, y1, x2, y2 = x1 + OFFSET, y1 + OFFSET, x2 + OFFSET, y2 + OFFSET

    for i in range(x1, x2):
        for j in range(y1, y2):
            checked[i][j] = n

mx1, my1, mx2, my2 = MAX_R, MAX_R, 0, 0
exist = False
for i in range(MAX_R + 1):
    for j in range(MAX_R + 1):
        if checked[i][j] == 1:
            exist = True
            mx1 = min(mx1, i)
            my1 = min(my1, j)
            mx2 = max(mx2, i)
            my2 = max(my2, j)

if not exist:
    print(0)
else:
    print((mx2 - mx1 + 1) * (my2 - my1 + 1))