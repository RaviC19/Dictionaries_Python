# pop - removes the key-value pair from the dictionary that matches the key you enter
d = dict(a=1, b=2, c=3)
d.pop("a")
print(d)  # {'b': 2, 'c': 3}

# popitem - removes and returns the last element (key, value) pair in a dictionary
e = dict(a=1, b=2, c=3, d=4, e=5)
e.popitem()
print(e)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# update - updates keys and values in a dictionary with another set of key value pairs
user = {
    "name": "Ravi",
    "location": "UK",
    "age": 30
}

person = {"language": "Python"}
person.update(user)
print(person)
# returns {'language': 'Python', 'name': 'Ravi', 'location': 'UK', 'age': 30}
