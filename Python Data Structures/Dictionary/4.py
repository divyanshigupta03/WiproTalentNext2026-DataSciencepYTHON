# write a program to iterate over a dictionary using for loop and print the keys alone, values alone and both keys and values
dict = {
    "name" : "Divyanshi",
    "age" : 21,
    "sem" : 6
}

print("Keys:")
for key in dict.keys():
    print(key)


print("Values:")
for values in dict.values():
    print(values)


print("Key-Value:")
for key,value in dict.items():
    print(f"{key}:{value}")
