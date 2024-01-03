n = int(input())
arr = list(map(int, input().split()))

min_val = arr[0]
cnt = 1

for elem in arr[1:]:
    if min_val > elem:
        min_val = elem
        cnt = 1
    elif min_val == elem:
        cnt += 1

print(min_val, cnt)