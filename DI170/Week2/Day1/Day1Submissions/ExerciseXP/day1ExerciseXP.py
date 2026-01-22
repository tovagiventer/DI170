# Exercise 1: Converting Lists into Dictionaries
# Instructions
# You are given two lists. Convert them into a dictionary where the first list contains the keys and the second list contains the corresponding values.

# Lists:
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

num_dict = {}
# num_dict.keys = [keys]
# num_dict.values = [values]
# for key in keys:
#     zip(keys, values)

num_dict = ({str(keys):str(values)})
print(num_dict)

