n = int(input())


def print_for(n):
    if n == 0:
        return

    print_for(n - 1)
    print(n, end=" ")


def print_back(n):
    if n == 0:
        return

    print(n, end=" ")
    print_back(n - 1)


print_for(n)
print()
print_back(n)