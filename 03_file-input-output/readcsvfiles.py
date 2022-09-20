# analyze.py
import csv

with open("filecounts.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile, fieldnames=["Folder", "CSV", "MD", "PNG"])
    counts = list(reader)

print(counts)


# You're operating your file object in read mode ("r")
# You're using the csv.DictReader() to read in the data.
# Since you didn't add a header row to your CSV data, you need to define what each piece of data refers to by passing a sequence to the argument fieldnames. These values will become the keys for the dictionary that'll get created from each row of your data.
# Finally, you need to convert the reader object to a list() in order to use it as expected.