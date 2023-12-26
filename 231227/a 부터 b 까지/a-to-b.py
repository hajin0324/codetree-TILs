inp = input().split()
a = int(inp[0])
b = int(inp[1])
i = a

while i <= b:
    print(i, end=" ")
    if i % 2 == 1:
        i *= 2
    else:
        i += 3