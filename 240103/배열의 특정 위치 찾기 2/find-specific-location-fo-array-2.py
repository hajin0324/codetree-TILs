arr = list(map(int, input().split()))
odd_sum = sum(arr[::2])
even_sum = sum(arr[1::2])

if odd_sum >= even_sum:
    print(odd_sum - even_sum)
else:
    print(even_sum - odd_sum)