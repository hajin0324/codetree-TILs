n = int(input())


def sequence(n):
    if n <= 2:
        return n

    return sequence(n // 3) + sequence(n - 1)


print(sequence(n))