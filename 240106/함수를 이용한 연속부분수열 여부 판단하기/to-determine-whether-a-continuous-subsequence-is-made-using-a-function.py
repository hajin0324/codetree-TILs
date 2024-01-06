def is_subsequence():
    for i in range(n1 - n2 + 1):
        if a[i:i + n2] == b:
            return True


n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

if is_subsequence():
    print("Yes")
else:
    print("No")