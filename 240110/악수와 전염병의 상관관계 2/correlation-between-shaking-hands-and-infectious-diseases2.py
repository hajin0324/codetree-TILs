N, K, P, T = map(int, input().split())
infection = [0] * (N + 1)
handshake = [list(map(int, input().split())) for _ in range(T)]

# 악수한 시간 순서대로 오름차순 정렬
handshake.sort(key=lambda x: x[0])

# 첫 번째 감염된 사람
infection[P] = 1

# 감염되어 있고, K 초과하지 않았다면 전염시킴
for t, x, y in handshake:
    if (infection[x] >= 1 and infection[x] <= K) or (infection[y] >= 1 and infection[y] <= K):
        infection[x] += 1
        infection[y] += 1

# 감염되었다면 1, 감염되지 않았다면 0 출력
for elem in infection[1:]:
    print(1 if elem >= 1 else 0, end="")