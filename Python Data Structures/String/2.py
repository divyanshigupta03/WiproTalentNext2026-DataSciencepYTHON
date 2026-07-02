# wap that will check whether a given String isPalindrome or not

str = "abccba"

def isPalindrome(str):
    i = 0
    j = len(str) - 1
    while i<=j:
        if str[i] == str[j]:
            return True
        else:
            return False
        
print(isPalindrome(str))
