n, m = map(int, input().split())

a = [0] * 1000000
b = [0] * 1000000

a_idx = 1
for _ in range(n):
    t, d = input().split()
    for _ in range(int(t)):
            a[a_idx] = a[a_idx - 1] + (1 if d == 'R' else -1)
            a_idx += 1

b_idx = 1
for _ in range(m):
    t, d = input().split()
    for _ in range(int(t)):
            b[b_idx] = b[b_idx - 1] + (1 if d == 'R' else -1)
            b_idx += 1

if a_idx > b_idx:
    for i in range(b_idx, a_idx):
        b[i] = b[i - 1]

elif b_idx > a_idx:
    for i in range(a_idx, b_idx):
        a[i] = a[i - 1]

cnt = 0
for i in range(1, max(a_idx, b_idx)):
    if a[i] == b[i] and a[i - 1] != b[i - 1]:
        cnt += 1

print(cnt)