# Given a person variable:
# Create a dictionary called answer , that makes each first item in each list a key and the second item a corresponding value. The end goal:
# {'name': 'Jared', 'job': 'Musician', 'city': 'Bern'}

person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]

answer = {i[0]: i[1] for i in person}
print(answer)

# Alternate solution 1
person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
answer = {k: v for k, v in person}
print(answer)

# Alternate solution 2 - If you have a list of pairs, you can very easily turn it into a dictionary using dict()
person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
answer = dict(person)
print(answer)
