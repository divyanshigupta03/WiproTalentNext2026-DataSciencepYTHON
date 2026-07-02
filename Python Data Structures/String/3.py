# given a string return a new string made of n copies of the first 2 chars of the original string where n is the length of the string . The string length will be >= 2. If input is "Wipro" then output should be "Wiwiwiwiwi"

str = input("Enter your String:")

result = str[:2] * len(str)

print(result)
