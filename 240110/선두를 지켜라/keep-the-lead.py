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

cnt = -1
f = 'o'
for i in range(1, 20000):

    if f != 'b' and a[i] < b[i]:
        cnt += 1
        f = 'b'
    elif f != 'r' and a[i] > b[i]:
        cnt += 1
        f = 'r'

print(cnt)