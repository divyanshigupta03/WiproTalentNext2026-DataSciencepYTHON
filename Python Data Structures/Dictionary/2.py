# write a program to concatenate the following dictionaries to create a new one
dict1 = {0:10 , 1:20}
dict2 = {2:30 , 3:40}
dict3 = {4:50 , 5:60}

new_dict = {}

new_dict.update(dict1)
new_dict.update(dict2)
new_dict.update(dict3)

print(new_dict)
