n, q = tuple(map(int, input().split()))
arr = list(map(int, input().split()))

for _ in range(q):
    que = list(map(int, input().split()))

    if que[0] == 1:
        a = que[1]
        print(arr[a - 1])

    elif que[0] == 2:
        a = que[1]
        if a in arr:
            print(arr.index(a) + 1)
        else:
            print(0)

    else:
        a, b = que[1], que[2]
        for i in range(a - 1, b):
            print(arr[i], end=" ")
        print()