class Student:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight


students = []
for _ in range(5):
    name, height, weight = input().split()
    students.append(Student(name, int(height), float(weight)))

students.sort(key=lambda x: x.name)
print("name")
for s in students:
    print(f"{s.name} {s.height} {s.weight:.1f}")

print()

students.sort(key=lambda x: -x.height)
print("height")
for s in students:
    print(f"{s.name} {s.height} {s.weight:.1f}")