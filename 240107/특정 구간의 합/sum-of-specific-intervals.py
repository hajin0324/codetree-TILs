n, m = map(int, input().split())
a = [0] + list(map(int, input().split()))


def part_sum(a1, a2):
    return sum(a[a1:a2 + 1])


for _ in range(m):
    a1, a2 = map(int, input().split())
    print(part_sum(a1, a2))