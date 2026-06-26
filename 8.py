# write a program to print the sum of all the digits of a given number
n = int(input("Enter Your Number"))

def sum(n):
    n = abs(n)
    sum = 0
    while n > 0:
     digit = n%10
     sum += digit
     n = n//10

    return sum

print(sum(n))

