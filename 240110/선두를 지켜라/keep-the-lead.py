n, m = map(int, input().split())

a = [0] * 2000000
b = [0] * 2000000

idx = 1
for i in range(n):
    v, t = map(int, input().split())

    for _ in range(t):
        a[idx] = a[idx - 1] + v
        idx += 1

idx = 1
for i in range(m):
    v, t = map(int, input().split())

    for _ in range(t):
        b[idx] = b[idx - 1] + v
        idx += 1

leader, cnt = 0, 0
for i in range(1, idx):
    if a[i] > b[i]:
        if leader == 2:
            cnt += 1
        leader = 1

    elif a[i] < b[i]:
        if leader == 1:
            cnt += 1
        leader = 2

print(cnt)