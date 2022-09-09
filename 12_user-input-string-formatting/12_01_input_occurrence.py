# Write a script that takes a string of words and a letter from the user.
# Find the index of first occurrence of the letter in the string. For example:
#
# String input: hello world
# Letter input: o
# Result: 4

words_input = input("Enter a phrase: ")
user_input = input("Enter one letter of the phrase: ")

print(words_input.find(user_input))
