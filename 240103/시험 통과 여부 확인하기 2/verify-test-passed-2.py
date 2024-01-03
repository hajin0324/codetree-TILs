n = int(input())
cnt = 0

for _ in range(n):
    score = list(map(int, input().split()))
    sum_val = sum(score)
    avg = sum_val / 4

    if avg >= 60:
        print("pass")
        cnt += 1
    else:
        print("fail")
        
print(cnt)