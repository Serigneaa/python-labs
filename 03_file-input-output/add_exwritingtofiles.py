# Above this would be your file counter code
# This code snippet assumes your saving the count
# to a dictionary called `count`, e.g.:
count = {'': 8, '.csv': 2, '.md': 2, '.png': 11}

# New code that writes to a file

# Create or open a file
file_out = open("filecounts.txt", "a") # 'append' mode

# Write your data to the file
file_out.write(str(count))
file_out.write("\n")  # Include a line break

# Close the file
file_out.close()
