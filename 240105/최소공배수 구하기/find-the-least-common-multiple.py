def find_lcm(n, m):
    lcm = n * m
    for i in range(max(n, m), n * m):
        if i % n == 0 and i % m == 0:
            lcm = i
            break
    print(lcm)


n, m = map(int, input().split())
find_lcm(n, m)