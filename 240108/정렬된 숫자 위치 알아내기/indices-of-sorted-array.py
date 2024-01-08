class Number:
    def __init__(self, number, index):
        self.number = number
        self.index = index


n = int(input())
arr = list(map(int, input().split()))
numbers = [Number(num, i) for i, num in enumerate(arr)]

numbers.sort(key=lambda x: (x.number, x.index))

idx = [0] * n
for i, num in enumerate(numbers, start=1):
    idx[num.index] = i

for i in idx:
    print(i, end=" ")