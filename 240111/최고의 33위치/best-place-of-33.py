n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

def get_coin_num(x, y):
    cnt = 0
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            if grid[i][j] == 1:
                cnt += 1

    return cnt


max_coin = 0
for i in range(n - 2):
    for j in range(n - 2):
        coin = get_coin_num(i, j)
        max_coin = max(max_coin, coin)

print(max_coin)