"""You are going to be given a word. Your job is to return the middle character of the word. If the word's length is odd, return the middle character. If the word's length is even, return the middle 2 characters.

#Examples:

Kata.getMiddle("test") should return "es"

Kata.getMiddle("testing") should return "t"

Kata.getMiddle("middle") should return "dd"

Kata.getMiddle("A") should return "A"""

def get_middle(s):
    length = len(s)
    middle_index = length // 2

    if length % 2 == 0:  # Even length
        return s[middle_index - 1: middle_index + 1]
    else:  # Odd length
        return s[middle_index]