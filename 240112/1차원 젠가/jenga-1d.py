n = int(input())
zenga = [int(input()) for _ in range(n)]

s1, e1 = map(int, input().split())
s2, e2 = map(int, input().split())

for i in range(s1 - 1, e1):
    zenga.pop(s1 - 1)

for i in range(s2 - 1, e2):
    zenga.pop(s2 - 1)

print(len(zenga))
for elem in zenga:
    print(elem)