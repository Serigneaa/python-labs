# Decipher the message within the `secret` variable.
# Pick out only the alphabetic characters, not the numbers.

secret = "2349h30023388281e3299371l1l3094842o0333322883"
solution = ""

for char in secret:
    if char.isalpha():
        solution += char

print(solution)

## First trial
# solution_1 = ""
# solution_2 = ""
# solution_3 = ""
# solution_4 = ""
# solution_5 = ""


# if secret[4] == "h":
#     solution_1 = secret[4]
#     print(solution_1)

# if secret[16] == "e":
#     solution_2 = secret[16]

# if secret[24] == "l":
#     solution_3 = secret[24]

# if secret[26] == "l":
#     solution_4 = secret[26]

# if secret[34] == "o":
#     solution_5 = secret[34]

# solution = solution_1 + solution_2 + solution_3 + solution_4 + solution_5
# print(solution)

