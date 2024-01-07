class Weather:
    def __init__(self, date, day, weather):
        self.date = date
        self.day = day
        self.weather = weather


n = int(input())
rain = Weather("9999-99-99", "", "")
for _ in range(n):
    date, day, weather = input().split()
    
    w = Weather(date, day, weather)
    if w.weather == "Rain":
        if rain.date >= w.date:
            rain = w

print(rain.date, rain.day, rain.weather)