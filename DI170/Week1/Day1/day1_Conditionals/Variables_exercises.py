# 1. ask the user to enter his/her name

# 2. use the len() function to check the lenght of the name. if it is less than 5 letter print('You have a short name :)')

# name = input("Enter your name.")
# if len(name) < 5:
#     print('You have a short name :)' )


# Ask the user for a number between 1 and 100

# If the number is a divisible by three, print Fizz

# If the number is a divisible by five, print Buzz.

# If the number is a divisible by both three and five, print FizzBuzz instead.

num = int(input("Enter a number between 1 and 100. "))
if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
elif num % 3 == 0:
    print("Fizz")
elif num % 5 == 0:
    print("Buzz")
    
# if (number) % 5 == 0 and (number) % 3 == 0:
#     print('FizzBuzz')
# elif (number) % 3 == 0 and (number) % 5 != 0:
#     print('Fizz')
# elif (number) % 5 == 0 and (number) % 3 != 0:
#     print('Buzz')


# You have a friend named Alice, and you want to send her a message with the following details:

# Name: Alice

# Age: 30

# City: New York

# Tasks:

# Use f-strings to print a message saying:

# "Hello, Alice! You are 30 years old and live in New York."

# Use str.format() to print the same message.

friend_name = ("Alice")
friend_age = 30
friend_city = ("New York")
print(f"Hello, {friend_name}! You are {friend_age} years old and live in {friend_city}.")
print("Hello, {}! You are {} years old and live in {}.".format(friend_name, friend_age, friend_city))


# Ask the user for their age using the input() function and store it in a variable age.

# Convert the inputted age into an integer and calculate the number of years until they turn 100.

# Display a message: "You will turn 100 in X years", where X is the number of years calculated.

user_age = int(input("Enter your age. "))
print(f"You will turn 100 in {100 - user_age} years.")