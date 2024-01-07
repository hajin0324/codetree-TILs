n = int(input())
arr = list(map(int, input().split()))

arr.sort()

max_val = 0
for i in range(n):
    sum_val = arr[i] + arr[2 * n - i - 1]
    if sum_val > max_val:
        max_val = sum_val

print(max_val)