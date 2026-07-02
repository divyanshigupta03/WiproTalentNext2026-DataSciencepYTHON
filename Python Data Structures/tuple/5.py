# wap to replace the last value of tuples in a list to 100
listOfTup = [(10,45,78) , (56,89,90) , (72, 90, 18, 67)]

for i in range(len(listOfTup)):
    listOfTup[i] = listOfTup[i][:-1] + (100,)

print(listOfTup)
