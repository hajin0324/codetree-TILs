inp = input().split()
a, b, c = int(inp[0]), int(inp[1]), int(inp[2])
satisfied = False

for i in range(a, b + 1):
    if i % c == 0:
        satisfied = True
        break
    
if satisfied:
    print("YES")
else:
    print("NO")