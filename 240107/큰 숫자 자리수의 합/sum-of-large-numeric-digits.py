a, b, c = map(int, input().split())


def each_sum(n):
    if n < 10:
        return n

    return (n % 10) + each_sum(n // 10)


print(each_sum(a * b * c))