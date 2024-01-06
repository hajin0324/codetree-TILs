def is_palindrome(s):
    reverse = s[::-1]
    if s == reverse:
        return True
    else:
        return False

    
s = input()
if is_palindrome(s):
    print("Yes")
else:
    print("No")