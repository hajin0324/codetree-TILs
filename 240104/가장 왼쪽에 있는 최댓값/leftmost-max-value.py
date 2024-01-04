n = int(input())
arr = list(map(int, input().split()))

max_val = 0
max_idx = n

while max_idx != 0:
    max_val = max(arr[:max_idx])
    max_idx = arr[:max_idx].index(max_val)
    print(max_idx + 1, end=" ")