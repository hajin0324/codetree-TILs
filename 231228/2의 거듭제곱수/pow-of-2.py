n = int(input())
x = 0

while True:
    if n == 1:
        print(x)
        break

    x += 1
    n //= 2