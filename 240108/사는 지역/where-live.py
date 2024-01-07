class Address:
    def __init__(self, name, address, region):
        self.name = name
        self.address = address
        self.region = region


n = int(input())
person = []
for _ in range(n):
    name, address, region = input().split()
    person.append(Address(name, address, region))

idx = 0
for i, p in enumerate(person):
    if p.name > person[idx].name:
        idx = i

print("name", person[idx].name)
print("addr", person[idx].address)
print("city", person[idx].region)