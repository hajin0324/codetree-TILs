rec = input().split()
w = int(rec[0])
h = int(rec[1])

w += 8
h *= 3

print(w, h, w * h, sep="\n")