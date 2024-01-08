m1, d1, m2, d2 = list(map(int, input().split()))
day = input()


def get_days(m, d):
    num_of_days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = d

    for i in range(1, m):
        day += num_of_days[i]

    return day


day1 = get_days(m1, d1)
day2 = get_days(m2, d2)

week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
day1 += week.index(day)

print((day2 - day1) // 7 + 1)