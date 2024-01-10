n = int(input())
x, y = 0, 0

mapper = {"E" : 0, "S" : 1, "W" : 2, "N" : 3}
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

time = 0
re = False

for _ in range(n):
    d, dist = input().split()
    dir_num, dist = mapper[d], int(dist)

    for i in range(dist):
        x, y = x + dxs[dir_num], y + dys[dir_num]
        time += 1

        if x == 0 and y == 0:
            re = True
            break

    if re:
        break

if re:
    print(time)
else:
    print(-1)