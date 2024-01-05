s = input()
s = list(s)

while len(s) != 1:
    idx = int(input())
    
    if idx >= len(s):
        idx = -1

    s.pop(idx)
    print(''.join(s))