n, m = map(int, input().split())

a = [0] * 100000
b = [0] * 100000

a_idx = 1
for _ in range(n):
    t, d = input().split()
    for i in range(int(t)):
            a[a_idx] = a[a_idx - 1] + (1 if d == 'R' else -1)
            a_idx += 1

b_idx = 1
for _ in range(n):
    t, d = input().split()
    for i in range(int(t)):
            b[b_idx] = b[b_idx - 1] + (1 if d == 'R' else -1)
            b_idx += 1

if a_idx > b_idx:
    for i in range(b_idx, a_idx - b_idx):
        b[i] = b[b_idx - 1]
    b_idx = a_idx

elif b_idx > a_idx:
    for i in range(a_idx, b_idx - a_idx):
        a[i] = a[a_idx - 1]
    a_idx = b_idx

cnt = -1
same = False
for i in range(1, a_idx):
    if not same and a[i] == b[i]:
        cnt += 1
    else:
        same = False
print(cnt)