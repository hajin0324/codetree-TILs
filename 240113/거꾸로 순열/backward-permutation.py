n = int(input())
visited = [False] * (n + 1)
ans = []


def print_ans():
    for elem in ans:
        print(elem, end=" ")
    print()


def choose(curr_num):
    if curr_num == n + 1:
        print_ans()
        return

    for i in range(n, 0, -1):
        if visited[i]:
            continue

        ans.append(i)
        visited[i] = True

        choose(curr_num + 1)

        ans.pop()
        visited[i] = False

    return

choose(1)