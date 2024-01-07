n = int(input())


def sequence(n):
    if n == 0:
        return 2
    
    if n == 1:
        return 4

    return sequence(n - 1) * sequence(n - 2) % 100


print(sequence(n - 1))