arr = list(map(int, input().split()))

even_sum = sum(arr[1::2])
three_avg = sum(arr[2::3]) / len(arr[2::3])

print(f"{even_sum} {three_avg:.1f}")