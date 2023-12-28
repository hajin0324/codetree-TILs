inp = input().split()
n, m = int(inp[0]), int(inp[1])

for _ in range(n):
    for _ in range(m):
        print("*", end=" ")
    print()