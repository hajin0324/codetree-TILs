def absolute_value(arr):
    for i in range(len(arr)):
        if arr[i] < 0:
            arr[i] = -arr[i]


n = int(input())
arr = list(map(int, input().split()))

absolute_value(arr)
for elem in arr:
    print(elem, end=" ")