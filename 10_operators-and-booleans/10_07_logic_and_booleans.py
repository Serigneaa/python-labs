# Demonstrate the use of all logical operators (and, or, not) below.
# Create variables that hold boolean values, then combine them
# to express the following sentence:
#
#   do two wrongs make a right?
# 
# Note that the truth value of the statement doesn't matter,
# but try to use all three logical operators in one line of code
# to get another boolean value as your result :)

wrong = False
right = True

result_1 = wrong and right
print(result_1)

result_2 = wrong or right
print(result_2)

result_3 = not wrong
print(result_3)

result_4 = not right
print(result_4)