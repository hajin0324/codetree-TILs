string = input()
alpha = input()
cnt = 0

for elem in string:
    if elem == alpha:
        cnt += 1

print(cnt)