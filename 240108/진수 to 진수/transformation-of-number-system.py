a, b = map(int, input().split())
n = input()


def get_a(a, n):
    num = 0

    for i in n:
        num = num * a + int(i)

    return num


def get_b(b, n):
    b_list = []

    while True:
        if n < b:
            b_list.append(n)
            break

        b_list.append(n % b)
        n //= b
    
    return b_list[::-1]


a_num = get_a(a, n)
b_num = get_b(b, a_num)

for i in b_num:
    print(i, end="")