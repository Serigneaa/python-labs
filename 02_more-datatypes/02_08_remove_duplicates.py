# Write code that removes all duplicates from a list.
# Solve this challenge in two ways:
# 1. Convert to a different data type
# 2. Use a loop and a second list to solve it more manually

list_ = [1, 2, 3, 4, 3, 4, 5]

# 1. solution : Convert to a different data type
list2 = set(list_)

print(list2)

# 2. Use a loop and a second list to solve it more manually

list3 = [1, 2, 3, 4, 5]

for list_ in list3:
    list_.append(list_.remove())

print(list_) 

# Almost done




