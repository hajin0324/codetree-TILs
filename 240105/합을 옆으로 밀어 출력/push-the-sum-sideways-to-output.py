n = int(input())
sum_val = 0

for _ in range(n):
    num = int(input())
    sum_val += num

s = str(sum_val)
s = s[1:] + s[0]

print(s)