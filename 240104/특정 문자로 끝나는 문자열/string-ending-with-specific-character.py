arr = [input() for _ in range(10)]
a = input()
cnt = 0

for elem in arr:
    if elem[len(elem) - 1] == a:
        print(elem)
        cnt += 1

if cnt == 0:
    print("None")