n = int(input())
block = [0] * 2000
idx = 1000

for _ in range(n):
    n, d = input().split()
    n = int(n)

    if d == 'R':
        for i in range(idx + 1, idx + n + 1):
            block[i] += 1
        idx += n

    else:
        for i in range(idx, idx - n, -1):
            block[i] += 1
        idx -= n

cnt = 0
for elem in block:
    if elem >= 2:
        cnt += 1

print(cnt)