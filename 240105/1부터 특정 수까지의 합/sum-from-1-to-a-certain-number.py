n = int(input())


def sum_div(n):
    sum_val = 0
    for i in range(1, n + 1):
        sum_val += i
    
    return sum_val // 10


print(sum_div(n))