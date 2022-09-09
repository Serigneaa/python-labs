# TODO: Write a prompt that asks users to "type something to win"
#       They will only win if they type "something" into the prompt
#
# Collect user input
# Compare to the string "something"
# Print a win or lose message

word = input("Type something to win:")
word = word.lower()
if word == "something":
    print("You won... nothing! :")
else:
    print("You lose")
