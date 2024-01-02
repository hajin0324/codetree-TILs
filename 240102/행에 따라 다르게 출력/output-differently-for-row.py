n = int(input())
cnt = 0

for i in range(n):
    for _ in range(n):
        if i % 2 == 0:
            cnt += 1
        else:
            cnt += 2
        print(cnt, end=" ")
    print()