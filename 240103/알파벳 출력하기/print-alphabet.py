n = int(input())
alpha = 'A'

for i in range(n):
    for j in range(i + 1):
        print(alpha, end="")
        alpha = chr(ord(alpha) + 1)
        if ord(alpha) > ord('Z'):
            alpha = 'A'
    print()