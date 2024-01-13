n, m = map(int, input().split())
ans = []

def print_ans():
    for elem in ans:
        print(elem, end=" ")
    print()


def choose(curr_num):
    if curr_num == m + 1:
        print_ans()
        return

    for i in range(1, n + 1):
        if i in ans or (curr_num != 1 and i <= ans[-1]):
            continue
        
        ans.append(i)
        choose(curr_num + 1)
        ans.pop()

    return

choose(1)