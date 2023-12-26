a = input().split()
a_age = int(a[0])
a_gen = a[1]

b = input().split()
b_age = int(b[0])
b_gen = b[1]

if (a_age >= 19 and a_gen == 'M') or (b_age >= 19 and b_gen == 'M'):
    print(1)
else:
    print(0)