a, b, c = map(int, input().split())

minute = 10 * 60 + 11
time = (a - 11) * 24 * 60 + (b - 1) * 60 + c
time -= minute

if time < 0:
    print(-1)
else:
    print(time)