s = input()
n = s.find('e')
s = s[:n] + s[n + 1:]
print(s)