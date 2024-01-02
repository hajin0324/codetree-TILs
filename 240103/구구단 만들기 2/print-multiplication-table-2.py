inp = input().split()
a, b = int(inp[0]), int(inp[1])

for i in range(2, 9, 2):
    for j in range(b, a - 1, -1):
        print(f"{j} * {i} = {j * i}", end=" ")
        if j != a:
            print("/", end=" ")
    print()