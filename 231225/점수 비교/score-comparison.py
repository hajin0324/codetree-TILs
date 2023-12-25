a = input().split()
b = input().split()

a_math = int(a[0])
a_eng = int(a[1])
b_math = int(b[0])
b_eng = int(b[1])

if a_math > b_math and a_eng > b_eng:
    print(1)
else:
    print(0)