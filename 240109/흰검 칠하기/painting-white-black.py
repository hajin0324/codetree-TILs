n = int(input())
tile = [[0, 0, 0] for _ in range(200000)]
idx = 100000

for _ in range(n):
    x, d = input().split()
    x = int(x)

    if d == 'L':
        for i in range(x):
            tile[idx - i][0] += 1
            tile[idx - i][2] = 1

        idx -= (x - 1)
    else:
        for i in range(x):
            tile[idx + i][1] += 1
            tile[idx + i][2] = 2

        idx += (x - 1)

white, black, gray = 0, 0, 0

for t in tile:
    if t[0] >= 2 and t[1] >= 2:
        gray += 1
    elif t[2] == 1:
        white += 1
    elif t[2] == 2:
        black += 1

print(white, black, gray)