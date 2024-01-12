n = int(input())
ans = []
cnt = 0


def is_beautiful():
    global n
    idx = 0

    while idx < n:
        if idx + ans[idx] - 1 >= n:
            return False

        for i in range(idx, idx + ans[idx]):
            if ans[idx] != ans[i]:
                return False

        idx += ans[idx]
        
    return True


def choose(curr_num):
    global cnt

    if curr_num > n:
        if is_beautiful():
            cnt += 1
        return

    for i in range(1, 5):
        ans.append(i)
        choose(curr_num + 1)
        ans.pop()

choose(1)
print(cnt)