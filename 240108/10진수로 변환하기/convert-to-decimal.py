n = list(map(int, list(input())))
num = 0

for i in range(len(n)):
    num = num * 2 + n[i]

print(num)