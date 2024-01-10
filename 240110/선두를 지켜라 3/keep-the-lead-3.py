n, m = map(int, input().split())

a = [0] * 1000000
b = [0] * 1000000

# 시간에 따른 A의 위치
a_idx = 1
for _ in range(n):
    v, t = map(int, input().split())
    for _ in range(t):
        a[a_idx] = a[a_idx - 1] + v 
        a_idx += 1

# 시간에 따른 B의 위치
b_idx = 1
for _ in range(m):
    v, t = map(int, input().split())
    for _ in range(t):
        b[b_idx] = b[b_idx - 1] + v
        b_idx += 1

leader, cnt = 0, 0
for i in range(1, a_idx):
    if a[i] > b[i] and leader != 1:
        leader = 1
        cnt += 1
    elif a[i] < b[i] and leader != 2:
        leader = 2
        cnt += 1
    elif a[i] == b[i] and leader != 3:
        leader = 3
        cnt += 1

print(cnt)