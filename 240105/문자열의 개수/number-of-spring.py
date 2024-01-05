cnt = 0
arr = []

while True:
    s = input()
    
    if s == '0':
        print(cnt)
        break

    arr.append(s)
    cnt += 1

for word in arr[::2]:
    print(word)