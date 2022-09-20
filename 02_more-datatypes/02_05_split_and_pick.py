# Write a script that takes in a string from the user.
# Using the `split()` method, create a list of all the words in the string
# and print back the most common word in the text.


counter = 0
sentence = input("Entrer une phrase:")

word_sentence = sentence.split()


print(word_sentence)

for word in word_sentence:
    counting = word_sentence.count(word)
    if counting > counter:
        counter = counting
        common_word = word

print(common_word) 

# DONE