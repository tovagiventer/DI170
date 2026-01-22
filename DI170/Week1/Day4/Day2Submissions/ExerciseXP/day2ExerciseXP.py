# # Exercise 1: Favorite Numbers
# # Create a set called my_fav_numbers and populate it with your favorite numbers.
# # Add two new numbers to the set.
# # Remove the last number you added to the set.
# # Create another set called friend_fav_numbers and populate it with your friend’s favorite numbers.
# # Concatenate my_fav_numbers and friend_fav_numbers to create a new set called our_fav_numbers.

# my_fav_numbers = {3, 7, 9, 1986, 1028}
# print(my_fav_numbers)
# my_fav_numbers.add(1856)
# my_fav_numbers.add(1379)
# print(my_fav_numbers)
# my_fav_numbers.remove(1379)
# print(my_fav_numbers)

# friend_fav_numbers = {9, 12, 17, 1950, 1983}
# our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
# print(our_fav_numbers)


# # Exercise 2: Tuple
# # Given a tuple of integers, try to add more integers to the tuple.
# # Hint: Tuples are immutable, meaning they cannot be changed after creation. Think about why you can’t add more integers to a tuple.

# tup = (1, 3, 7, 9)
# # tup.add(5)
# print(tup)


# # Exercise 3: List Manipulation
# # You have a list: basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# # Remove "Banana" from the list.
# # Remove "Blueberries" from the list.
# # Add "Kiwi" to the end of the list.
# # Add "Apples" to the beginning of the list.
# # Count how many times "Apples" appear in the list.
# # Empty the list.
# # Print the final state of the list.

# basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# basket.remove('Banana')
# basket.remove('Blueberries')
# basket.append('Kiwi')
# basket.insert(0, 'Apples')
# print(basket.count('Apples'))
# basket.clear()
# print(basket)


# # Exercise 4: Floats
# # Recap: What is a float? What’s the difference between a float and an integer?
# # Create a list containing the following sequence of mixed types: floats and integers:
# # 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5.
# # Avoid hard-coding each number manually.
# # Think: Can you generate this sequence using a loop or another method?

# num = 1.5
# halves = []
# while num <= 5:
#     halves.append(num)
#     num += 0.5
# print(halves)

# # num = 1.5
# # l = []
# # while num <= 5:
# #     l.append(num)
# #     num += 0.5
# # print(l)

# # halves = list(range(1.5, 5.5, 0.5))
# # print (halves)


# Exercise 5: For Loop
# Write a for loop to print all numbers from 1 to 20, inclusive.
# Write another for loop that prints every number from 1 to 20 where the index is even.

# for num in range(1, 21):
#     print(num)
# for even_num in range(1, 21):
#     if even_num % 2 == 0:
#         print(even_num)


# # Exercise 6: While Loop
# # Use an input to ask the user to enter their name.
# # Using a while True loop, check if the user gave a proper name (not digits and at least 3 letters long)
# # hint: check for the method isdigit()
# # if the input is incorrect, keep asking for the correct input until it is correct
# # if the input is correct print “thank you” and break the loop

# while True:
#     name = input('Enter your name. ')

#     found_digit = False 
#     for char in name:
#         if char.isdigit():
#             found_digit = True
#             break
        
#     if len(name) >= 3 and not found_digit:
#         break
    
#     print('Please enter a correct name. ')

# print('Thank you. ')

## name = input('Enter your name. ')
## for ch in name:
##     print(ch, ch.isdigit())


# # Exercise 7: Favorite Fruits
# # Ask the user to input their favorite fruits (they can input several fruits, separated by spaces).
# # Store these fruits in a list.
# # Ask the user to input the name of any fruit.
# # If the fruit is in their list of favorite fruits, print:
# # "You chose one of your favorite fruits! Enjoy!"
# # If not, print:
# # "You chose a new fruit. I hope you enjoy it!"

# fav_fruits = []
# fav_fruits = input('What are some of your favorite fruits? ')
# fruit = input('Pick a fruit. ')
# if fruit in fav_fruits:
#     print('You chose one of your favorite fruits! Enjoy!')
# else:
#     print('You chose a new fruit. I hope you enjoy it!')


# #  Exercise 8: Pizza Toppings
# # Write a loop that asks the user to enter pizza toppings one by one.
# # Stop the loop when the user types 'quit'.
# # For each topping entered, print:
# # "Adding [topping] to your pizza."
# # After exiting the loop, print all the toppings and the total cost of the pizza.
# # The base price is $10, and each topping adds $2.50.

# topping = []
# while True: 
#     toppings = input("Please add a pizza topping, or enter 'quit' when you are finished. ") 
#     if toppings == 'quit':
#         break
#     else:
#         topping.append(toppings)
#         print(f'Adding {topping[-1]} to your pizza. ')

# print(topping)
# print(f'Your total is ${2.5*len(topping) + 10}')


# # Exercise 9: Cinemax Tickets
# # Ask for the age of each person in a family who wants to buy a movie ticket.
# # Calculate the total cost based on the following rules:
# # Free for people under 3.
# # $10 for people aged 3 to 12.
# # $15 for anyone over 12.
# # Print the total ticket cost.


# ticket_under3 = 0
# ticket_3to12 = 0
# ticket_over12 = 0

# while True: 
#     ticket = input("Please enter the age of each person buying a movie ticket, one at a time, or enter 'quit' when you are finished.")
#     if ticket == 'quit':
#         break
#     elif int(ticket) < 3:
#         ticket_under3 +=1
#     elif int(ticket) <= 12:
#         ticket_3to12 +=1
#     else:
#         ticket_over12 +=1

# print(f'Your total ticket cost is ${10*ticket_3to12 + 15*ticket_over12}')

total_cost = 0
while True:
    ticket = input("Please enter the age of each person buying a movie ticket, one at a time, or enter 'quit' when you are finished.")
    if ticket == 'quit':
        break
    ticket_age = int(ticket)
    if ticket_age > 3 and ticket_age <= 12:
        total_cost += 10
    elif ticket_age > 12:
        total_cost += 15

print(f'Your total ticket cost is ${total_cost}')