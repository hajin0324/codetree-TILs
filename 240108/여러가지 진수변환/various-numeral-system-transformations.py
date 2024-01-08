n, b = map(int, input().split())
binary = []

while True:
    if n < b:
        binary.append(n)
        break

    binary.append(n % b)
    n //= b

for n in binary[::-1]:
    print(n, end="")