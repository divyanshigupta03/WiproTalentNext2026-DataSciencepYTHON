# given a string and an integer n, return a string made of n repetitions of the last n characters of the string. You may assume that n is between and the length of the string inclusive. For example if the inputs are "Wipro" and 3, then the output should be "propropro"

str = input("Enter your String:")
n = int(input("Enter your Number:"))

s = str[-n:] * n

print(s)
