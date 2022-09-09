# Write a script that takes a string of words and a symbol from the user.
# Replace all occurrences of the first letter with the symbol. For example:
#
# String input: more python programming please
# Symbol input: §
# Result: §ore python progra§§ing please

words_input = input("Enter a phrase: ")
user_input = input("Enter a symbol: ")

first_letter = words_input[0]
words_input.replace(first_letter, user_input)
print(words_input)

# Work In Progress

