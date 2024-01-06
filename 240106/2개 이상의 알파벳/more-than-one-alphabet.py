def other(a):
    for i in range(len(a)):
        if a[i] != a[0]:
            return True

    return False


s = input()

if other(s):
    print("Yes")
else:
    print("No")