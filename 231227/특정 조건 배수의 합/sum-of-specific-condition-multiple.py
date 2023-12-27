inp = input().split()
a, b = int(inp[0]), int(inp[1])
sum_val = 0

if a > b:
    a, b = b, a

for i in range(a, b + 1):
    if i % 5 == 0:
        sum_val += i

print(sum_val)