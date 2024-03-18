# You need to write a function, that returns the first non-repeated character in the given string.

# If all the characters are unique, return the first character of the string.
# If there is no unique character, return None.

# You can assume, that the input string has always non-zero length.

# Examples
# "test"   returns "e"
# "teeter" returns "r"
# "trend"  returns "t" (all the characters are unique)
# "aabbcc" returns None (all the characters are repeated)

def solution(string):
    letter_count = {}
    for letter in string:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    for letter in string:
        if letter_count[letter] == 1:
            return letter
    return None

def solution(string1):
    empty_letter = []
    repeated_letters = []
    for letter in string1:
        if letter in empty_letter:
            repeated_letters.append(letter)
        else:
            empty_letter.append(letter)
    for letter in empty_letter:
        if letter not in repeated_letters:
            return letter


from collections import Counter


def solution(inputstr):
    # Make a counter of characters that have been seen
    count_dict = Counter(inputstr)
    for i in inputstr:
        if count_dict[i] == 1:
            return i
    return None

def solution(string):
    for char in string:
        if string.count(char) == 1:
            return char
    return None
