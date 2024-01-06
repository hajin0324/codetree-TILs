def is_prime(n):
    if n == 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False   
            
    return True


def sum_even(n):
    sum_val = 0
    while n > 0:
        sum_val += n % 10
        n //= 10
    
    if sum_val % 2 == 0:
        return True
    else:
        return False


a, b = map(int, input().split())
cnt = 0

for i in range(a, b + 1):
    if is_prime(i) and sum_even(i):
        cnt += 1

print(cnt)