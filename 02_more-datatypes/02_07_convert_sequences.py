# Convert some sequences you got to know into other sequences:
# - Convert the string shown below into a tuple.
# - Convert the tuple into a list.
# - Change the `c` character in your list into a `k`
# - Convert the list back into a tuple.

string = "codingnomads"
atuple = tuple(string)
alist = list(atuple)

alist[0] = "k"
atuple2 = tuple(alist)

print(string)
print(atuple)
print(alist)
print(atuple2)


