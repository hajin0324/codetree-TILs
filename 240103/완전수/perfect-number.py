start, end = tuple(map(int, input().split()))
ans = 0

for num in range(start, end + 1):
    
    sum_val = 0
    for divisor in range(1, num):
        if num % divisor == 0:
           sum_val += divisor
    
    if sum_val == num:
        ans += 1

print(ans)