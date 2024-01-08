class People:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight


n = int(input())
peoples = []
for _ in range(n):
    name, height, weight = input().split()
    peoples.append(People(name, int(height), int(weight)))

peoples.sort(key=lambda x: x.height)

for p in peoples:
    print(p.name, p.height, p.weight)