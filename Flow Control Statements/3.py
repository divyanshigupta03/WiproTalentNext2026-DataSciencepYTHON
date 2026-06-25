# Given two non-negative values, print true if they have the same last digit, such as with 27 and 57
n1 = int(input("Enter First No:"))
n2 = int(input("Enter Second No:"))

def evenOdd(n1,n2):
    if(n1%10 == n2%10):
        return True
    else:
        return False
    

result = evenOdd(n1,n2)
print(result)