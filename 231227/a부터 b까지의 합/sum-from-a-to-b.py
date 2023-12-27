inp = input().split()
a = int(inp[0])
b = int(inp[1])
sum_val = 0

for i in range(a, b + 1):
    sum_val += i

print(sum_val)