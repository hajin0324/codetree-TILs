clinic = [0] * 4

for _ in range(3):
    arr = input().split()
    if arr[0] == 'Y' and int(arr[1]) >= 37:
        clinic[0] += 1
    elif int(arr[1]) >= 37:
        clinic[1] += 1
    elif arr[0] == 'Y':
        clinic[2] += 1
    else:
        clinic[3] += 1

for elem in clinic:
    print(elem, end=" ")

if clinic[0] >= 2:
    print("E")