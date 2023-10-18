# https://www.codewars.com/kata/5656b6906de340bd1b0000ac/train/python

"""
Take 2 strings s1 and s2 including only letters from a to z. Return a new sorted string, the longest possible, containing distinct letters - each taken only once - coming from s1 or s2.

Examples:
a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
longest(a, b) -> "abcdefklmopqwxy"

a = "abcdefghijklmnopqrstuvwxyz"
longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"
"""

"""
def longest(a1, a2):
    testString = "abcdefghijklmnopqrstuvwxzy"
    sortedString = []
    for i in testString:
        if i in (a1 + a2):
            sortedString.append(i)
    return ''.join(sortedString)
longest("aretheyhere", "yestheyarehere")
"""
def longest(a1, a2):
    newString = ""
    for i in a1 + a2:
        if i not in (newString):
            newString += i
    print(''.join(sorted(newString)))
longest("aretheyhere", "yestheyarehere")