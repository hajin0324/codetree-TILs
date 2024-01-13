k, n = map(int, input().split())
ans = []

def print_ans():
    for elem in ans:
        print(elem, end=" ")
    print()

def choose(curr_num):
    if curr_num == n:
        print_ans()
        return

    for i in range(1, k + 1):
        if curr_num >= 2 and i == ans[-1] and i == ans[-2]:
            continue
        
        ans.append(i)
        choose(curr_num + 1)
        ans.pop()

    return

choose(0)