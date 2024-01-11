n, m = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]


def happy_num(a, b):
    global n, m

    for i in range(m - 1):
        if grid[a][b + i] != grid[a][b + i + 1]:
            return False
    return True


ans = 0
for i in range(n):
    for j in range(n - m + 1):
        if m == 1:
            ans += 2
            break

        for k in range(m - 1):
            if grid[i][j + k] != grid[i][j + k + 1]:
                break
            ans += 1

        for k in range(m - 1):
            if grid[j][i + k] != grid[j][i + k + 1]:
                break
            ans += 1
            
print(ans)