n, m = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]


def happy_num(x, y):
    global m
    for i in range(y + m):
        if grid[x][y] != grid[x][y + 1]:
            return False
    return True


ans = 0
for i in range(n - m + 1):
    for j in range(n - m + 1):
        if happy_num(i, j) or happy_num(j, i):
            ans += 1

print(ans)