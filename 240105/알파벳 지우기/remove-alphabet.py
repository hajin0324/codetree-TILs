s1 = input()
s2 = input()

n1 = ""
n2 = ""

for elem in s1:
    if elem.isdigit():
        n1 += elem

for elem in s2:
    if elem.isdigit():
        n2 += elem

print(int(n1) + int(n2))