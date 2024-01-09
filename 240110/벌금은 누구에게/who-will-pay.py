n, m, k = map(int, input().split())
fine = [0] * (n + 1)

idx = -1
for i in range(m):
    num = int(input())

    fine[num] += 1

    if fine[num] >= k:
        idx = num
        break

print(idx)