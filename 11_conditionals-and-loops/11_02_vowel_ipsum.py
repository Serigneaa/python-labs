# Print the total number of vowels that are used in the lorem ipsum text.

lorem_ipsum = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut 
aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in 
voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt 
mollit anim id est laborum."""

vowel_a = 0
vowel_o = 0
vowel_i = 0
vowel_u = 0
vowel_e = 0

if "a" in lorem_ipsum:
    vowel_a = lorem_ipsum.count("a")

if "o" in lorem_ipsum:
    vowel_o = lorem_ipsum.count("o")

if "i" in lorem_ipsum:
    vowel_i = lorem_ipsum.count("i")

if "u" in lorem_ipsum:
    vowel_u = lorem_ipsum.count("u")

if "e" in lorem_ipsum:
    vowel_e = lorem_ipsum.count("e")

print(vowel_a + vowel_o + vowel_i + vowel_u + vowel_e)



