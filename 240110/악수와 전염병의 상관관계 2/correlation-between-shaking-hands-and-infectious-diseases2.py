n, k, p, t = map(int, input().split())
infection = [0] * (n + 1)
handshake = [list(map(int, input().split())) for _ in range(t)]
handshake.sort(key=lambda x: x[0])
infection[p] = 1

for s, x, y in handshake:
    if infection[x] >= 1 and infection[x] < t or infection[y] >= 1 and infection[y] < t:
        infection[x] += 1
        infection[y] += 1

for elem in infection[1:]:
    if elem >= 1:
        elem = 1
    print(elem, end="")