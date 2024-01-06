def leap_year(y):
    if y % 400 == 0:
        return True
    elif y % 100 == 0:
        return False
    elif y % 4 == 0:
        return True
    
    return False


def last_day(y, m):
    if m == 2:
        if leap_year(y):
            return 29
        else:
            return 28
    elif m == 2 or m == 4 or m == 6 or m == 9 or m == 11:
        return 30
    
    return 31


def judge_day(y, m, d):
    if d <= last_day(y, m):
        return True
    
    return False


def weather(m):
    if 3 <= m and m <= 5:
        return "Spring"
    elif 6 <= m and m <= 8:
        return "Summer"
    elif 9 <= m and m <= 11:
        return "Fall"
    else:
        return "Winter"


y, m, d = map(int, input().split())

if judge_day(y, m, d):
    print(weather(m))
else:
    print(-1)