# https://www.codewars.com/kata/554b4ac871d6813a03000035/train/python

def high_and_low(numbers):
    intNumbers = []
    for i in numbers.split(" "):
        intNumbers.append(int(i))
    return f'{max(intNumbers)} {min(intNumbers)}'
high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4")