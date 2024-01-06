def plus(a, c):
    return a + c


def minus(a, c):
    if a < c:
        a, c = c, a
    return a - c


def divide(a, c):
    return a // c


def times(a, c):
    return a * c


a, o, c = input().split()
a, c = int(a), int(c)

if o == '+':
    print(a, "+", c, "=", plus(a, c))
elif o == '-':
    print(a, "-", c, "=", minus(a, c))
elif o == '/':
    print(a, "/", c, "=", divide(a, c))
elif o == '*':
    print(a, "*", c, "=", times(a, c))
else:
    print("False")