# Use a loop to add together all the donations and store the resulting number of the total value in a variable called total_donations
donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5,
                 stan=150.0, lisa=50.25, harrison=10.0)

total_donations = 0

for value in donations.values():
    total_donations += value
print(total_donations)

# This solution uses a built-in function called sum() which I cover in the "Lambdas and Built-In Functions" section
total_donations = sum(donation for donation in donations.values())

# An even better solution using the same sum built-in function is just this nice little line:
total_donations = sum(donations.values())
