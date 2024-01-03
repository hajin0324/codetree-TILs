n1, n2 = map(int,input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

for i in range(n1 - n2 + 1):
    part = True
    for j in range(n2):
        if a[i + j] != b[j]:
            part = False
            break
    if part:
        break

if part:
    print("Yes")
else:
    print("No")