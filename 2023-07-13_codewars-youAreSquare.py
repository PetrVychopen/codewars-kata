# https://www.codewars.com/kata/54c27a33fb7da0db0100040e/train/python
# Square numbers always end with the digits 0, 1, 4, 5, 6, and 9.
import math
def is_square(n):
    if n < 0:
        return False
    elif math.sqrt(n) ** 2 == n:
        print(True)
    else:
        print(False)
is_square(-9)

# TO DO