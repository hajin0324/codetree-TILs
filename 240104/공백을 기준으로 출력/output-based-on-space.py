str1 = input()
str2 = input()

for elem in str1 + str2:
    if elem == " ":
        continue
    print(elem, end="")