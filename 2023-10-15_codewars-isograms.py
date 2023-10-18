# https://www.codewars.com/kata/54ba84be607a92aa900000f1/train/python

"""
An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

Example: (Input --> Output)

"Dermatoglyphics" --> true "aba" --> false "moOse" --> false (ignore letter case)

isIsogram "Dermatoglyphics" = true
isIsogram "moose" = false
isIsogram "aba" = false
"""

def is_isogram(string):
    sum = 0

    string_lower = string.lower()
    string_len = len(string_lower)

    for i in string_lower:
        sum += string_lower.count(i)

    if sum <= string_len:
        return True
    else:
        return False
is_isogram("")