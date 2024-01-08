class Dot:
    def __init__(self, x, y, number):
        self.x = x
        self.y = y
        self.number = number


n = int(input())
dots = []
for i in range(n):
    x, y = map(int, input().split())
    dots.append(Dot(x, y, i + 1))

dots.sort(key=lambda x: (abs(x.x) + (abs(x.y))))

for d in dots:
    print(d.number)