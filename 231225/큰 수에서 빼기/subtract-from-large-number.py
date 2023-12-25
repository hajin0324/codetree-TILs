arr = input().split()
a = int(arr[0])
b = int(arr[1])

if a < b:
    a, b = b, a

print(a - b)