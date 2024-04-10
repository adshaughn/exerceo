# Given a string s consisting of words and spaces, return the length of the last word in the string.
#
# A word is a maximal
# substring
# consisting of non-space characters only.
#
#
#
# Example 1:
#
# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.
# Example 2:
#
# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.
# Example 3:
#
# Input: s = "luffy is still joyboy"
# Output: 6
# Explanation: The last word is "joyboy" with length 6.

import re


def lengthOfLastWord(s) -> int:
    # step 1 - remove trailing spaces from string

    cleaned_s = s.strip()

    # step 2 - use regex to isolate last word
    last_word = re.search("[A-Za-z]+$", cleaned_s)

    lwo = last_word.group()

    # step 3 - get lenght of last word

    length_lw = len(lwo)

    # step 4 - return length

    return length_lw
