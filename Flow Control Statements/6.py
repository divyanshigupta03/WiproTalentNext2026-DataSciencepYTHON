# Write a program to check if a given no is prime or not
n = int(input("Enter Your Number:"))

def is_Prime(n):
    if(n <= 1):
        return False
    
    if(n == 2):
        return True
    
    if(n % 2 == 0):
        return False
    limit = int(n**0.5) + 1
    for i in range(3, limit, 2):
        if n % i == 0:
            return False
        
    return True


print(is_Prime(n))
