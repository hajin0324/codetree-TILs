n, k, t = input().split()
n, k = int(n), int(k)


def start_t(s, t):
    if len(s) < len(t):
        return False

    return s[:len(t)] == t


arr = []
for _ in range(n):
    word = input()
    if start_t(word, t):
        arr.append(word)

arr.sort()
print(arr[k - 1])