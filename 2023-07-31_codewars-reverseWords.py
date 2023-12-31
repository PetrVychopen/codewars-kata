# https://www.codewars.com/kata/5259b20d6021e9e14c0010d4/train/python

"""
Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.

Examples
"This is an example!" ==> "sihT si na !elpmaxe"
"double  spaces"      ==> "elbuod  secaps"
"""

def reverse_words(text):
    reversed_text = ""
    for i in text.split(" "):
        reversed_text = reversed_text + " " + i[::-1]
    return reversed_text.strip()
reverse_words("This is an example!")