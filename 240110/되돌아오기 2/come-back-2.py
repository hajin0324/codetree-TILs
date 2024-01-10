commands = input()
x, y = 0, 0

dir_num = 3
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

ans = 0
re = False
for c in commands:
    ans += 1
    if c == 'L':
        dir_num = (dir_num - 1 + 4) % 4
    elif c == 'R':
        dir_num = (dir_num + 1) % 4
    else:
        x, y = x + dxs[dir_num], y + dys[dir_num]

        if x == 0 and y == 0:
            re = True
            break

if re:
    print(ans)
else:
    print(-1)