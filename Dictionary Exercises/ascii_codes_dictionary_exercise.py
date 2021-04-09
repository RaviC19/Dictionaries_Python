# Every character has an ASCII code (basically, a number that represents it)
# Python has a function called chr() that will return a string if you provide the corresponding integer ASCII code
# For example:
# chr(65)  will return  'A'
# chr(66)  will return  'B'
# All the way up to:
# chr(90)  will return  'Z'

# Create dictionary that maps ASCII keys to their corresponding letters.  Use a dictionary comprehension and chr()
# Save the result to the answer variable. You only need to care about capital letters (65-90).

answer = {num: chr(num) for num in range(65, 91)}
print(answer)
