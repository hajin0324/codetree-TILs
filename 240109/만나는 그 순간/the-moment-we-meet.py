n, m = map(int, input().split())

a_move = [0 for _ in range(10000)]
b_move = [0 for _ in range(10000)]

idx = 1
for _ in range(n):
    d, c = input().split()
    
    for _ in range(int(c)):
        a_move[idx] = a_move[idx - 1] + (1 if d == 'R' else -1)
        idx += 1

idx = 1
for _ in range(m):
    d, c = input().split()

    for _ in range(int(c)):
        b_move[idx] = b_move[idx - 1] + (1 if d == 'R' else -1)
        idx += 1

meet = -1
for i in range(1, 10000):
    if a_move[i] == b_move[i]:
        meet = i
        break

print(meet)