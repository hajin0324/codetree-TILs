n1, n2 = map(int, input().split())
num = n1 + n2
cnt = 0

for elem in str(num):
    if elem == '1':
        cnt += 1

print(cnt)