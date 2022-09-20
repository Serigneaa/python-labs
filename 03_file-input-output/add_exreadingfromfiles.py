# Above this would be your file counter code
# This code snippet assumes your saving the count
# to a dictionary called `count`, e.g.:
count = {'': 8, '.csv': 2, '.md': 2, '.png': 11}

# New code that writes to a file

# Create or open a file
file_in = open("filecounts.txt", "r")

# Read data from the file
contents = file_in.read()

# Close the file
file_in.close()

# Print out the value of contents.
print(contents)

# What data type does contents have?
print(type(contents))