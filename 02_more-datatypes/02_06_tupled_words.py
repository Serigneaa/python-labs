# Write a script that takes a string from the user
# and creates a list that contains a tuple for each word.
# For example:

# input = "hello world"
# result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]

char_sentence = []
sentence = input("Entrer une phrase:")
word_sentence = sentence.split()


print(word_sentence)
print(type(word_sentence))

for word in word_sentence:
    for letter in word:
        char_sentence.append(letter)

print(char_sentence)

# Almost Done

