n = int(input())

for num in range(1, n + 1):
    if num == 1:
        continue
    
    isprime = True
    for divisor in range(2, num):
        if num % divisor == 0:
            isprime = False
        
    if isprime:
        print(num, end=" ")