"""
Challenge: Number to Alphabet

Given a number N, return the first N letters of the alphabet (A-Z).
"""


def number_to_alphabet(num):
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    letters_up_to_num = alphabet[:num]
    print(letters_up_to_num)


number_to_alphabet(13)
