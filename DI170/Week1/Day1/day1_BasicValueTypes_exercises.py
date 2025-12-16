# description = "strings are..."

# make it all uper case
# replace the word "are" to "is"
# print just the word "strings"

description = "strings are..."
upper_string = description.upper
print(upper_string)

replaced = description.replace('are', 'is')
print(replaced)

# splice code?
print(description[0:7])


# In the python shell, Create a variable called my_age, use python to know how old you will be in 123879 years

my_age = 39
aged = my_age + 123879
print(aged)

# Check what is the type of each value, then change it: if it is a string, make it an integer and vice-versa:

bank_balance = '33000'
phone_number = 532287514

print(type(bank_balance))
print(type(phone_number))

bank_balance = int(bank_balance)
phone_number = str(phone_number)

print(type(bank_balance))
print(type(phone_number))

# In the python shell, Create a variable called first_name and a variable called last_name, and then print your full name using those two variables

first_name = "Tova"
last_name = "Giventer"

print(first_name + " " + last_name)


# Given the following values:

x = 5
y = 10
z = 0
word1 = "hello"
word2 = "world"

# 1. Check if x is less than y and y is greater than z.
print(x < y and y > z)
# 2. Verify if word1 is not equal to word2.
print(word1 != word2)
# 3. Use the bool() function to check the boolean value of z and word1.
print(bool(z))
print(bool(word1))

