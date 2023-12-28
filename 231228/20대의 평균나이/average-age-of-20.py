cnt = 0
sum_val = 0

while True:
    age = int(input())

    if age >= 30 or age <= 19:
        print(f"{sum_val / cnt:.2f}") 
        break

    cnt += 1
    sum_val += age