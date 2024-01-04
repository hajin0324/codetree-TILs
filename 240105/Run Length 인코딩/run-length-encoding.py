a = input()
encoded = ''

pre = a[0]
cnt = 1

for i in range(1, len(a)):
    if a[i] == pre:
        cnt += 1
    else:
        encoded += pre
        encoded += str(cnt)

        pre = a[i]
        cnt = 1

encoded += pre
encoded += str(cnt)

print(len(encoded))
print(encoded)