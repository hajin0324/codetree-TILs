n = int(input())
alpha = 'A'

for _ in range(n):
    for _ in range(n):
        print(alpha, end="")
        alpha = chr(ord(alpha) + 1)
    print()