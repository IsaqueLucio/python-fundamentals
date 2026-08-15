"""
Challenge: Text to Number Cipher

Convert each letter of a text into its corresponding position in the
alphabet (A=1, B=2, C=3, ..., Z=26).
"""

def text_to_number_cipher(text):
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    counter = 0
    result = []
    for i in range(len(text)):
        for j in range(len(letters)):
            if text[i] != letters[j]:
                counter += 1
            else:
                counter += 1
                result.append(counter)
                counter = 0
                break

    return result

print(text_to_number_cipher("M"))
