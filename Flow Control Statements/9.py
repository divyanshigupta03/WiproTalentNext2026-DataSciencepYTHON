# write a program to print the reverse of given no
n = int(input("Enter Your Number"))

def reverse(n):
    while n>0:
        digit = n%10
        print(digit,end="")
        n = n//10

reverse(n)
