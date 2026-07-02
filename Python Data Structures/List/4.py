# write a program to print the no of occurrences of a specified element in a list

list = [2,1,5,2,6,2,7,2]

count = 0
for i in list:
    if i == 2:
        count += 1

print(count)
