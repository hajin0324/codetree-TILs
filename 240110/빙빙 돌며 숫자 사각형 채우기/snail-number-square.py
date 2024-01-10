n, m = map(int, input().split())
x, y = 0, 0
answer = [
    [0 for _ in range(m)]
    for _ in range(n)
]

dir_num = 0
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]


def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m


answer[x][y] = 1
for i in range(2, n * m + 1):
    nx, ny = x + dxs[dir_num], y + dys[dir_num]

    if not in_range(nx, ny) or answer[nx][ny] != 0:
        dir_num = (dir_num + 1) % 4

    x, y = x + dxs[dir_num], y + dys[dir_num]
    answer[x][y] = i

for row in answer:
    for elem in row:
        print(elem, end=" ")
    print()