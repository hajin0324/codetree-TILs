n = int(input())
arr = [n * i for i in range(1, 11)]

cnt = 0
for elem in arr:
    print(elem, end=" ")

    if elem % 5 == 0:
        cnt += 1
    if cnt == 2:
        break