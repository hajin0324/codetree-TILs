m1, d1, m2, d2 = map(int, input().split())


def get_days(m, d):
    num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = d
    
    for i in range(1, m):
        day += num_of_days[i]

    return day


day1 = get_days(m1, d1)
day2 = get_days(m2, d2)

print(day2 - day1 + 1)