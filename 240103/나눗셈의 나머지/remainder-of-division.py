a, b = tuple(map(int, input().split()))
count_arr = [0] * 10

while a > 1:
    count_arr[a % b] += 1
    a //= b

sum_val = 0
for elem in count_arr:
    sum_val += elem ** 2

print(sum_val)