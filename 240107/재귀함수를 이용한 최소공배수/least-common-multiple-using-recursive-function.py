n = int(input())
arr = list(map(int, input().split()))


def calc(a, b):
    for i in range(min(a, b), 0, -1):
        if a % i == 0 and b % i == 0:
            return (a * b) // i

    return a * b


def get_lcm(n):
    if n == 0:
        return arr[0]

    return calc(get_lcm(n - 1), arr[n])


print(get_lcm(n - 1))