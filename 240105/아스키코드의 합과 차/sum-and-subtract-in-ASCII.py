a, b = input().split()
a_asc = ord(a)
b_asc = ord(b)

print(a_asc + b_asc, end=" ")

if a_asc > b_asc:
    print(a_asc - b_asc)
else:
    print(b_asc - a_asc)