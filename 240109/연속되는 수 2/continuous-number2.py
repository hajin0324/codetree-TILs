n = int(input())

cnt = 0
pre = -1
max_cnt = 0

for i in range(n):
    num = int(input())

    if i == 0 or num == pre:
        cnt += 1
    else:
        cnt = 1

    pre = num
    max_cnt = max(max_cnt, cnt)
        
print(max_cnt)