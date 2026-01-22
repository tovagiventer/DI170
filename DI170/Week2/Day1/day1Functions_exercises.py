# Write a function calculation() such that it can accept two variables and calculate the addition and subtraction of it. And also it must return both addition and subtraction in a single return call

def calculation(a, b):
    return(a-b, a+b)

minus, plus = calculation(40, 10)
print (minus, plus)
print (calculation)

people = ["Rick", "Morty", "Beth", "Jerry", "Snowball"]
# Using map and filter, try to say hello to everyone who's name is less than or equal to 4 letters
    
filtered_list = list(filter(lambda name: len(name) <= 4, people))
print(filtered_list)

mapped = list(map(lambda name: f'hello {name}', filtered_list))
print(mapped)

# The fixed final exercise:

# people = ["Rick", "Morty", "Beth", "Jerry", "Snowball"]

# # Using map and filter, try to say hello to everyone who's name is less than or equal to 4 letters

# filtered_list = list(filter(lambda name: len(name) <= 4, people))
# print(filtered_list)

# mapped = list(map(lambda name: f"hello {name}", filtered_list))
# print(mapped)

