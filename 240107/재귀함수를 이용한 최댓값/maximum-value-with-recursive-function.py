n = int(input())
arr = list(map(int, input().split()))


def get_max(idx):
    if idx == 0:
        return arr[idx]
    
    return max(arr[idx], get_max(idx - 1))


print(get_max(n - 1))