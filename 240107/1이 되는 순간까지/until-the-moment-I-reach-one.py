n = int(input())


def get_num(n):
    if n == 1:
        return 0

    if n % 2 == 0:
        return 1 + get_num(n // 2)
    else:
        return 1 + get_num(n // 3)


print(get_num(n))