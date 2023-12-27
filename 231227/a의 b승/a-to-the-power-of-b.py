inp = input().split()
a = int(inp[0])
b = int(inp[1])
prod = 1

for _ in range(b):
    prod *= a

print(prod)