n = int(input())
block = [0] * 101

for _ in range(n):
    x1, x2 = map(int, input().split())

    for i in range(x1, x2 + 1):
        block[i] += 1

print(max(block))