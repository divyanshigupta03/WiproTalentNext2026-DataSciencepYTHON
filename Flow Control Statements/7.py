# Write a program to prime numbers between 10 and 99
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


for i in range(10,100):
    if is_Prime(i):
        print(i , end = " ")