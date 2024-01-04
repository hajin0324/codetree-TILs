string = input()
n = int(input())

if len(string) < n:
    print(string[::-1])
else:
    print(string[-1:-1-n:-1])