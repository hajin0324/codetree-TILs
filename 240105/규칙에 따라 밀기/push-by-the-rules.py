a = input()
c = input()

for elem in c:
    if c == 'L':
        a = a[1:] + a[0]
    else:
        a = a[-1] + a[:-1]

print(a)