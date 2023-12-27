n = int(input())
i = 1

while n > 1:
    i += 1
    n //= i

print(i)