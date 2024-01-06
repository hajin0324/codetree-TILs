n, m = map(int, input().split())
a = list(map(int, input().split()))


def cal():
    global n, m
    sum_val = a[m - 1]

    while m != 1:
        if m % 2 != 0:
            m -= 1
        else:
            m //= 2

        sum_val += a[m - 1]
    
    return sum_val


print(cal())