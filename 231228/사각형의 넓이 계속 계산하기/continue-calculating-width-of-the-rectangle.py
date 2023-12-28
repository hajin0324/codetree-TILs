while True:
    inp = input().split()
    w, h, c = int(inp[0]), int(inp[1]), inp[2]

    print(w * h)

    if c == 'C':
        break