# clear
user = {
    "name": "Ravi",
    "location": "UK",
    "age": 30
}
user.clear()
print(user)  # returns {}

# copy
numbers = dict(a=1, b=2, c=3)
dupe = numbers.copy()
print(dupe)  # {'a': 1, 'b': 2, 'c': 3}
dupe == numbers  # True
dupe is numbers  # returns False because they are unique objects in memory and not stored in the same place

# fromkeys - creates key-value pairs from comma separated values and is only used on an item object {}
player = {}.fromkeys(["name", "score", "age", "location"], "unknown")
# would return {'name': 'unknown', 'score': 'unknown', 'age': 'unknown', 'location': 'unknown'}
print(player)

# get - if a key is in a dictionary it will return the value, if it doesn't exist it will return as None
me = {
    "name": "Ravi",
    "location": "UK",
    "age": 30
}

me.get("name")  # Ravi
me.get("phone number")  # Wouldn't return anything but is None
