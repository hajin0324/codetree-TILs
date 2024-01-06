string = input()
sub = input()

def sub_idx():
    for i in range(len(string) - len(sub) + 1):
        if string[i:i + len(sub)] == sub:
            return i

    return -1


print(sub_idx())