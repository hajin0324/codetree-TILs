inp = input().split()
a = int(inp[0])
b = int(inp[1])

if a >= 1:
    for _ in range(b):
        print(a, end="")
else:
    print(0)