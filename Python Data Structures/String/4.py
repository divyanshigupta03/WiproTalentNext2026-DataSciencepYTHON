# given a string, if the first or last character is 'x' , return the string without those 'x' character, else return the string unchanged. If the input is "xHix", then output is "Hi"
str = input("Enter Your string:")

if str.startswith('x'):
    s = str[1:]

if str.endswith('x'):
    s = str[:-1]

print(s)
