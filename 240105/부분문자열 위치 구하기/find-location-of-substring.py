s = input()
p = input()

part = False
for i in range(len(s) - len(p) + 1):
    if s[i:i + len(p)] == p:
        part = True
        print(i)
        break

if not part:
    print(-1)