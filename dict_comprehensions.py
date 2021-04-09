# iterates over keys by default
# to iterate over kys and values use .items()

numbers = dict(first=1, second=2, third=3)
squared_numbers = {key: value ** 2 for key, value in numbers.items()}
print(squared_numbers)
# returns {'first': 1, 'second': 4, 'third': 9}

user = {
    "name": "Ravi",
    "location": "United Kingdom",
    "colour": "Brown"
}

yelling_user = {key.upper(): value.upper() for key, value in user.items()}
print(yelling_user)

# conditional logic with dictionaries
num_list = [1, 2, 3, 4, 5]
{num: ("even" if num % 2 == 0 else "odd") for num in num_list}
{num: ("even" if num % 2 == 0 else "odd") for num in range(1, 20)}

user2 = {
    "name": "Ravi",
    "location": "United Kingdom",
    "colour": "Brown"
}

yelling_colour = {key.upper() if key is "colour" else key: value.upper()
                  for key, value in user2.items()}
print(yelling_colour)
