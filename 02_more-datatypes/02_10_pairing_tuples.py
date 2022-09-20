# The import below gives you a new random list of numbers,
# called `randlist`, every time you run the script.
#
# Write a script that takes this list of numbers and:
#     - sorts the numbers
#     - stores the numbers in tuples of two in a new list
#     - prints each tuple
#
# If the list has an odd number of items,
# add the last item to a tuple together with the number `0`.
#
# Note: This lab might be challenging! Make sure to discuss it 
# with your mentor or chat about it on our forum.

from resources import randlist

list_1 = []
new_list = []
print(randlist)

# Write your code below here
list_1 = randlist.sort()
list_1 = list(list_1)

print(type(list_1))

#new_list = [tuple[::2] for tuple in list_1]

#print(new_list)