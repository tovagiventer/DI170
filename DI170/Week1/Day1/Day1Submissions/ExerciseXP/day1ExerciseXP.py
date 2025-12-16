# Exercise 1: Hello World
# Print the following output using one line of code:
# Hello world
# Hello world
# Hello world
# Hello world

for i in range(4):
    print("Hello world")


# Exercise 2: Some Math
# Write code that calculates the result of:
# (99^3)*8 (meaning 99 to the power of 3, times 8).

print((99**3)*8)


# Exercise 3: What is the output?
# Predict the output of the following code snippets:
# Coment what is your guess, then run the code and compare

print(5 < 3) #False 
print(3 == 3) #True
print(3 == "3") #False
# print("3" > 3) #TypeError
print("Hello" == "hello") #False


#  Exercise 4: Your computer brand
# Create a variable called computer_brand which value is the brand name of your computer.
# Using the computer_brand variable, print a sentence that states the following:
# "I have a <computer_brand> computer."

computer_brand = 'Lenovo'
print(f'I have a {computer_brand} computer.')


# Exercise 5: Your information
# Create a variable called name, and set it’s value to your name.
# Create a variable called age, and set it’s value to your age.
# Create a variable called shoe_size, and set it’s value to your shoe size.
# Create a variable called info and set it’s value to an interesting sentence about yourself. The sentence must contain all the variables created in parts 1, 2, and 3.
# Have your code print the info message.
# Run your code.

name = 'Tova'
age = 39
shoe_size = 41
info = (f'My name is {name}, I am {age} years old, and I wear size {shoe_size} shoes.')
print(info)


# Exercise 6: A & B
# Create two variables, a and b.
# Each variable’s value should be a number.
# If a is bigger than b, have your code print "Hello World".

a = int(input("Enter a number. "))
b = int(input("Enter another number. "))
if a > b:
    print('Hello World')


# Exercise 7: Odd or Even
# Write code that asks the user for a number and determines whether this number is odd or even.

num = int(input('Enter a number. '))
if (num) % 2 == 0:
    print('Even')
else:
    print('Odd')


#  Exercise 8: What’s your name?
# Write code that asks the user for their name and determines whether or not you have the same name. Print out a funny message based on the outcome.

name = input('What\'s your name? ')
if name == 'Tova':
    print('Hey! That\'s my name, too!')
else:
    print('Well, that\'s a nice name too, I suppose.')


# Exercise 9: Tall enough to ride a roller coaster
# Write code that will ask the user for their height in centimeters.
# If they are over 145 cm, print a message that states they are tall enough to ride.
# If they are not tall enough, print a message that says they need to grow some more to ride.

height = int(input('How tall are you, in centimeters? '))
if height > 145:
    print('You are tall enough to ride the roller coaster.')
else:
    print('You need to grow a little more.')
