a = input()
c = input()

for elem in c:
    if elem == 'L':
        a = a[1:] + a[0]
    else:
        a = a[-1] + a[:-1]

print(a)