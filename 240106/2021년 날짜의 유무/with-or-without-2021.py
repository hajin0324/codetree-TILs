def last_day(m):
    if m == 2:
        return 28
    elif m == 2 or m == 4 or m == 6 or m == 9 or m == 11:
        return 30

    return 31


def judge_day(m, d):
    if m <= 12 and d <= last_day(m):
        return True

    return False


m, d = map(int, input().split())

if judge_day(m, d):
    print("Yes")
else:
    print("No")