n = int(input())


def get_demical(n):
    bi = 1
    trans = 0

    while n > 0:
        trans += (n % 10) * bi
        bi *= 2
        n //= 10

    return trans


def get_binary(n):
    digits = []

    while True:
        if n < 2:
            digits.append(n)
            break
        
        digits.append(n % 2)
        n //= 2

    for i in digits[::-1]:
        print(i, end="")


n = get_demical(n) * 17
get_binary(n)