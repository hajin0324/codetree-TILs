s = input()

idx = len(s) - 1
if idx % 2 == 0:
    idx -= 1

for i in range(idx, -1, -2):
    print(s[i], end="")