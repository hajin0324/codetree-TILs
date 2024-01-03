n = int(input())

for i in range(n):
    m = int(input())

    cnt = 0
    while m != 1:
        if m % 2 == 0:
            m //= 2
        else:
            m = m * 3 + 1
        cnt += 1

    print(cnt)