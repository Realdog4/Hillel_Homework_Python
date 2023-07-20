"""
Count the number of Duplicates
Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.

Example
"abcde" -> 0 # no characters repeats more than once
"aabbcde" -> 2 # 'a' and 'b'
"aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
"indivisibility" -> 1 # 'i' occurs six times
"Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
"aA11" -> 2 # 'a' and '1'
"ABBA" -> 2 # 'A' and 'B' each occur twice
"""


def count_duplicates(input_string):
    char_count = {}
    for char in input_string.lower():
        if char.isalpha() or char.isdigit():
            char_count[char] = char_count.get(char, 0) + 1

    duplicate_count = sum(1 for count in char_count.values() if count > 1)
    return duplicate_count


print(count_duplicates("abcde"))
print(count_duplicates("aabbcde"))
print(count_duplicates("aabBcde"))
print(count_duplicates("indivisibility"))
print(count_duplicates("Indivisibilities"))
print(count_duplicates("aA11"))
print(count_duplicates("ABBA"))