arr = input().split()
a = int(arr[0])
b = int(arr[1])
c = int(arr[2])

n_sum = a + b + c
avg = n_sum // 3

print(n_sum, avg, n_sum - avg, sep="\n")