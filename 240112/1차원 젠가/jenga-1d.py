n = int(input())
zenga = [int(input()) for _ in range(n)]
temp = [0] * n

for _ in range(2):
    s, e = map(int, input().split())
    for i in range(s - 1, e):
        zenga[i] = 0
    
    idx = 0
    for n in zenga:
        if n != 0:
            temp[idx] = n
            idx += 1

    zenga = temp[:]

print(idx)
for elem in zenga[:idx]:
    print(elem)