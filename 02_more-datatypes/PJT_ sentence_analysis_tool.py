#Write a script that takes a sentence from the user and returns:

#the number of lower case letters
#the number of uppercase letters
#the number of punctuations characters
#the total number of characters
#Use a dictionary to store the count of each of the above.

#Note: ignore all spaces.

from curses.ascii import islower
import string

counter = {"lower" : 0, "upper" : 0, "number_punc" : 0, "number_char" : 0}


sentence = input("Enter a sentence:")

for word in sentence:
    for letter in word:

        if letter.isupper():
            counter["upper"] += 1
        
        elif letter.islower():
            counter["lower"] += 1

        elif letter == " ":
            continue

        else: 
            letter in string.punctuation
            counter["number_punc"] += 1

counter["number_char"] = counter["lower"] + counter["upper"] + counter["number_punc"]
counter.update()
print(counter.items())

# Almost DONE


        

