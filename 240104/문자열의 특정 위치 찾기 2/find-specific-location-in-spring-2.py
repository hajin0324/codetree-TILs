arr = ["apple", "banana", "grape", "blueberry", "orange"]

n = input()
cnt = 0

for elem in arr:
    if elem[2] == n or elem[3] == n:
        print(elem)
        cnt += 1

print(cnt)