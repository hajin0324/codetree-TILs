n, t = map(int, input().split())
u = list(map(int, input().split()))
d = list(map(int, input().split()))
d = d[::-1]

for _ in range(t):
    temp = d[n - 1]
    d[n - 1] = u[n - 1]

    for i in range(n - 1, 0, -1):
        u[i] = u[i - 1]
    u[0] = d[0]

    for i in range(0, n - 2):
        d[i] = d[i + 1]
    d[n - 2] = temp

for elem in u:
    print(elem, end=" ")
print()

for elem in d[::-1]:
    print(elem, end=" ")