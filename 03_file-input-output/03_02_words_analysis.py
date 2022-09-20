# Read in all the words from the `words.txt` file.
# Then find and print:

# 1. The shortest word (if there is a tie, print all)
# 2. The longest word (if there is a tie, print all)
# 3. The total number of words in the file.

from itertools import count
from pathlib import Path

lw_counter = 15
sw_counter = 3
counter = 0
all_shortest_words = []
all_longest_words = []
longest_word = ""
shortest_word = ""


data_path = Path("/home/serigne/Desktop/DS & ML Engineering/Codingnomads/4. python-201-main/03_file-input-output")

with open(data_path.joinpath("words.txt"), "r") as file_in:
    
    for word in file_in:
        counter += 1
        
        # 1. The shortest word (if there is a tie, print all)
        if len(word) >= lw_counter:
            longest_word = word

            if len(word) > lw_counter:
                all_longest_words = []

            elif len(word) == lw_counter:
                all_longest_words.append(word)
            
            lw_counter = len(word)

        # 2. The longest word (if there is a tie, print all)
        if len(word) <= sw_counter:
            shortest_word = word

            if len(word) < sw_counter:
                all_shortest_words = []

            elif len(word) == sw_counter:
                all_shortest_words.append(word)

            sw_counter = len(word)

print("\n".join(all_longest_words))
print("\n".join(all_shortest_words))
print(counter)



