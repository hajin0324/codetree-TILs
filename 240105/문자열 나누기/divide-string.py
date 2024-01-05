n = int(input())
arr = input().split()
string = ''.join(arr)

for i in range(len(string)):
    print(string[i], end="")

    if (i + 1) % 5 == 0:
        print()