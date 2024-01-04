arr_2d = [
    input().split()
    for _ in range(5)
]

for row in arr_2d:
    for elem in row:
        print(chr(ord(elem) + ord('A') - ord('a')), end=" ")
    print()