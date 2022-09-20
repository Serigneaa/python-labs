# Write a function named `stats()` that takes in a list of numbers
# and finds the maximum, minimum, average and sum of the numbers.
# Print these values to the console you call the function.

example_list = [1, 2, 3, 4, 5, 6, 7]


def stats():
  # define the function here
  min_num = min(example_list)
  print(min_num)
  max_num = max(example_list)
  print(max_num)
  avr_num = sum(example_list)/len(example_list)
  print(avr_num)
  sum_num = sum(example_list)
  print(sum_num)

# call the function below here
stats()
