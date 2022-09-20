import csv
# -- snip --
count = {"": 8, ".csv": 2, ".md": 2, ".png": 11}

with open("filecounts.csv", "a") as csvfile:
    countwriter = csv.writer(csvfile)
    data = [count[""], count[".csv"], count[".md"], count[".png"]]
    countwriter.writerow(data)

# First, you're importing the csv module from Python's standard library.
# Then you're using a context manager to open up a file in append mode ("a"), and saving the file object to the variable csvfile.
# Next, you're creating a CSV writer object with the opened csvfile as its input, and you save it to the variable csvwriter.
# Now you're preparing the row of data that you want to write to the file. For this, you're accessing each piece of information through a dictionary lookup and adding them to a list.
# file_inally, you're using the csvwriter to write the row of data to your file using .writerow().