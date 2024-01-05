s, q = input().split()
s = list(s)
q = int(q)

for _ in range(q):
    arr = input().split()

    if arr[0] == '1':
        a, b = int(arr[1]), int(arr[2])
        s[a - 1], s[b - 1] = s[b - 1], s[a - 1]
    else:
        for i in range(len(s)):
            if s[i] == arr[1]:
                s[i] = arr[2]

    print(''.join(s))