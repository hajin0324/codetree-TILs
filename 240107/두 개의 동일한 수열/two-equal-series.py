n = int(input())
a = list(map(int ,input().split()))
b = list(map(int ,input().split()))


def equal(n):
    for i in range(n):
        if a[i] != b[i]:    
            return False

    return True


a.sort()
b.sort()

if equal(n):
    print("Yes")
else:
    print("No")