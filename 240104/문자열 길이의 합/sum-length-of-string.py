n = int(input())
leng = 0
a_cnt = 0

for i in range(n):
    string = input()
    leng += len(string)

    if string[0] == 'a':
        a_cnt += 1

print(leng, a_cnt)