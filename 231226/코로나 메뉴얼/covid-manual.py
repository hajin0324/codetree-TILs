per1 = input().split()
c1, t1 = per1[0], int(per1[1])

per2 = input().split()
c2, t2 = per2[0], int(per2[1])

per3 = input().split()
c3, t3 = per3[0], int(per3[1])

if c1 == 'Y' and t1 >= 37:
    if (c2 == 'Y' and t2 >= 37) or (c3 == 'Y' and t3 >= 37):
        print("E")
    else:
        print("N")
else:
    if (c2 == 'Y' and t2 >= 37) and (c3 == 'Y' and t3 >= 37):
        print("E")
    else:
        print("N")