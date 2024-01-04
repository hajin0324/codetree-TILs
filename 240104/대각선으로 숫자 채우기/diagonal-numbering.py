n, m = map(int, input().split())
arr = [[0 for _ in range(m)] for _ in range(n)]
num = 1

for i in range(n):
    for j in range(m):
        if arr[i][j] != 0:
            continue

        arr[i][j] = num
        num += 1

        cnt = 1
        while True:
            rx, ry = i + cnt, j - cnt
            if rx >= n or ry < 0 or arr[rx][ry] != 0:
                break
            
            arr[rx][ry] = num
            cnt += 1
            num += 1

for row in arr:
    for elem in row:
        print(elem, end=" ")
    print()