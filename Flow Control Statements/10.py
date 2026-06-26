# check whether the given no is palindrome or not
n = int(input("Enter Your Number:"))

def is_Palindrome(n):
    return str(n) == str(n)[::-1]
