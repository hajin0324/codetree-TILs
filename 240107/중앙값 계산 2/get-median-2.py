n = int(input())
arr = list(map(int, input().split()))

for i in range(n):
    if i % 2 == 0:
        curr_arr = sorted(arr[:i + 1])
        print(curr_arr[i // 2], end=" ")