# Write a script that reads in the contents of `words.txt`
# and writes the contents in reverse to a new file `words_reverse.txt`.


from pathlib import Path

contents = []
r_contents = []

data_path = Path("/home/serigne/Desktop/DS & ML Engineering/Codingnomads/4. python-201-main/03_file-input-output")

with open(data_path.joinpath("words.txt"), "r") as file_in:
    for word in file_in.readlines():
        word = word.rstrip()
        contents.append(word)
    
print(contents)

for w in contents[::-1]:
    r_contents.append(w)

with open(data_path.joinpath("words_reverse.txt"), "w") as file_out:
    file_out.write("\n".join(r_contents))


