n, t = map(int, input().split())
r, c, d = input().split()
x, y = int(r) - 1, int(c) - 1

d_list = {"R" : 0, "D" : 1, "U" : 2, "L" : 3}
dxs, dys = [0, 1, -1, 0], [1, 0, 0, -1]
dir_num = d_list[d]


def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n


for _ in range(t):
    nx, ny = x + dxs[dir_num], y + dys[dir_num]

    if not in_range(nx, ny):
        dir_num = 3 - dir_num
    else:
        x, y = x + dxs[dir_num], y + dys[dir_num]

print(x + 1, y + 1)