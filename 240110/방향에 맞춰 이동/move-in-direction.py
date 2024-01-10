n = int(input())
x, y = 0, 0

d_list = {"E" : 0, "S" : 1, "W" : 2, "N" : 3}
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]

for _ in range(n):
    d, c = input().split()
    d, c = d_list[d], int(c)

    x += dx[d] * c 
    y += dy[d] * c

print(x, y)