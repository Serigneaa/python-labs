# Write a program that reads in `words.txt` and prints only the words
# that have more than 20 characters (not counting whitespace).

from pathlib import Path

long_words = []

data_path = Path("/home/serigne/Desktop/DS & ML Engineering/Codingnomads/4. python-201-main/03_file-input-output")

with open(data_path.joinpath("words.txt"), "r") as file_in:
    
    for word in file_in:
        if len(word) >= 20:
            long_words.append(word)

print("\n".join(long_words))



