n = int(input())
col = [0] * 20000
curr = 10000

for _ in range(n):
    x, d = input().split()
    x = int(x)

    if d == 'L':
        for i in range(x):
            col[curr + i] = 1
        curr += (x - 1)
    else:
        for i in range(x):
            col[curr - i] = 2
        curr -= (x - 1)

white, black = 0, 0
for c in col:
    if c == 1:
        white += 1
    elif c == 2:
        black += 1

print(white, black)