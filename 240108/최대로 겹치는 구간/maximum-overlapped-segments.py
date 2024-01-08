OFFSET = 100

n = int(input())
line = [0] * 201

for _ in range(n):
    x1, x2 = map(int, input().split())
    x1, x2 = x1 + OFFSET, x2 + OFFSET
    
    for i in range(x1, x2):
        line[i] += 1

print(max(line))