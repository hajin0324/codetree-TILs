n = int(input())


def sequence(n):
    if n == 1:
        return 0

    if n % 2 == 0:
        return 1 + sequence(n // 2)
    else:
        return 1 + sequence(n * 3 + 1)


print(sequence(n))