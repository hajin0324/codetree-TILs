n1, n2 = map(int,input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

part = True
for i in range(n1 - n2):
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