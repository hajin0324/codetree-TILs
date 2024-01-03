n = int(input())
arr = [1, n]
cnt = 2

while True:
    arr.append(arr[cnt - 1] + arr[cnt - 2])
    if arr[cnt] > 100:
        break
    cnt += 1

for elem in arr:
    print(elem, end=" ")