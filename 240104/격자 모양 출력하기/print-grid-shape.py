n, m = map(int, input().split())
placed = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

for _ in range(m):
    r,c = map(int, input().split())
    placed[r][c] = r * c

for row in placed[1: n + 1]:
    for elem in row[1: n + 1]:
        print(elem, end=" ")
    print()