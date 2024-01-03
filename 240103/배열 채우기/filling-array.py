arr = list(map(int, input().split()))
cnt = len(arr) - 1

for i in range(len(arr)):
    if arr[i] == 0:
        cnt = i - 1

for i in range(cnt, -1, -1):
    print(arr[i], end=" ")