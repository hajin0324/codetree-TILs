s = input()
sum_val = 0

for elem in s:
    if elem.isdigit():
        sum_val += int(elem)

print(sum_val)