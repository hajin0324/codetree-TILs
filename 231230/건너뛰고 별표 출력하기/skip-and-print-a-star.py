n = int(input())

for i in range(n):
    for _ in range(i + 1):
        print("*", end="")
    print()
    print()

for i in range(n - 1, 0, -1):
    for _ in range(i):
        print("*", end="")
    print()
    print()