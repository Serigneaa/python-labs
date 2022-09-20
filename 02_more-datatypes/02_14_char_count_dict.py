# Write a script that takes a text input from the user
# and creates a dictionary that maps the letters in the string
# to the number of times they occur. For example:
#
# user_input = "hello"
# result = {"h": 1, "e": 1, "l": 2, "o": 1}

result = {}

user_sentence = input("Enter a sentence:")
for word in user_sentence:
    for letter in word:
        word_number = user_sentence.count(letter)
        if letter in result.keys():
            continue
        else:
            result[letter] = word_number

print(result)
