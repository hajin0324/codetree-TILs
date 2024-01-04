n = int(input())
arr = [input() for _ in range(n)]
a = input()

cnt = 0
leng = 0

for elem in arr:
    if elem[0] == a:
        cnt += 1
        leng += len(elem)

print(f"{cnt} {leng / cnt:.2f}")