cnt = 0
sum_val = 0

for _ in range(10):
    n = int(input())
    if 0 <= n and n <= 200:
        cnt += 1
        sum_val += n

print(f"{sum_val} {sum_val / cnt:.1f}")