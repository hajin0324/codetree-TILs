s = input()
fir = s[0]
sec = s[1]

for i in range(len(s)):
    if s[i] == fir:
        s = s[:i] + sec + s[i + 1:]
    elif s[i] == sec:
        s = s[:i] + fir + s[i + 1:]

print(s)