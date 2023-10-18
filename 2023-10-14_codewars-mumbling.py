# https://www.codewars.com/kata/5667e8f4e3f572a8f2000039/train/python

"""
accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"
The parameter of accum is a string which includes only letters from a..z and A..Z.
"""

def accum(s):
  accumulator = ""
  for i in range(len(s)):
    accumulator += s[i] * (i + 1)
    if i < len(s) - 1:
      accumulator += "-"
  print(accumulator)
accum("abcd")

# TODO capitalize first letter