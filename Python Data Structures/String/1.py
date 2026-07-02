# wap to count the number of upper and lower case letters in a String

str = input("Enter the String:")

upper = 0
lower = 0

for i in str:
    if i.isupper():
        upper += 1
    elif i.islower():
        lower += 1

for i in str:
    if str.islower():
        lower += 1

print("Upper = " , upper)
print("Lower=" , lower)
