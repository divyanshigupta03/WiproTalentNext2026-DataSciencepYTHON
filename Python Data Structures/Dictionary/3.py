# wap to check if a given key already exists in a dictionary
dict = {
    "name" : "Divyanshi",
    "age" : 21,
    "sem" : 6
}

key = "age"

if key in dict:
    print(f"The key {key} exists in the dict")
else:
     print(f"The key {key} does not exist in the dict")
