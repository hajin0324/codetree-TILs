a = input()
b = input()


while True:
    part = False
    for i in range(len(a) - len(b) + 1):
        if a[i:i + len(b)] == b:
            a = a[:i] + a[i + len(b):]
            part = True
            break

    if not part:
        break

print(a)